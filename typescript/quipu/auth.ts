/**
 * OAuth2 client_credentials flow for Quipu API.
 *
 * Provides a QuipuAuth middleware that transparently handles
 * token exchange and refresh. Inject it into the generated API classes
 * via Configuration middleware.
 */

import { Configuration, Middleware, FetchParams, RequestContext } from "../quipu_client/src/runtime";
import * as apis from "../quipu_client/src/apis/index";

const BASE_URL = "https://getquipu.com";

interface TokenResponse {
  access_token: string;
  token_type: string;
  expires_in: number;
  scope: string;
  created_at: number;
}

/**
 * Middleware that manages Quipu's OAuth2 client_credentials flow.
 *
 * Automatically fetches a Bearer token on first request and refreshes
 * it 60 seconds before expiry.
 */
export class QuipuAuth implements Middleware {
  private appId: string;
  private appSecret: string;
  private baseUrl: string;
  private scope: string;
  private accessToken: string | null = null;
  private expiresIn = 0;
  private tokenAcquiredAt = 0;

  constructor(options?: {
    appId?: string;
    appSecret?: string;
    baseUrl?: string;
    scope?: string;
  }) {
    this.appId = options?.appId ?? requireEnv("QUIPU_APP_ID");
    this.appSecret = options?.appSecret ?? requireEnv("QUIPU_APP_SECRET");
    this.baseUrl = options?.baseUrl ?? BASE_URL;
    this.scope = options?.scope ?? "ecommerce";
  }

  private get tokenExpired(): boolean {
    if (this.accessToken === null) return true;
    const elapsed = (Date.now() / 1000) - this.tokenAcquiredAt;
    return elapsed >= this.expiresIn - 60;
  }

  private async fetchToken(): Promise<void> {
    const body = new URLSearchParams({
      grant_type: "client_credentials",
      scope: this.scope,
    });

    const resp = await fetch(`${this.baseUrl}/oauth/token`, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        Authorization: "Basic " + btoa(`${this.appId}:${this.appSecret}`),
      },
      body,
    });

    if (!resp.ok) {
      throw new Error(`Token request failed: ${resp.status} ${resp.statusText}`);
    }

    const data: TokenResponse = await resp.json();
    this.accessToken = data.access_token;
    this.expiresIn = data.expires_in ?? 7200;
    this.tokenAcquiredAt = Date.now() / 1000;
  }

  async pre(context: RequestContext): Promise<FetchParams | void> {
    if (this.tokenExpired) {
      await this.fetchToken();
    }

    return {
      url: context.url,
      init: {
        ...context.init,
        headers: {
          ...context.init.headers,
          Authorization: `Bearer ${this.accessToken}`,
        },
      },
    };
  }
}

function requireEnv(name: string): string {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Environment variable ${name} is required`);
  }
  return value;
}

/**
 * Create a Configuration with auto-refreshing OAuth2 auth.
 *
 * Usage:
 *   const config = createConfig();
 *   const contactsApi = new ContactsApi(config);
 *   const contacts = await contactsApi.getContacts();
 */
export function createConfig(options?: {
  appId?: string;
  appSecret?: string;
  baseUrl?: string;
  scope?: string;
}): Configuration {
  const auth = new QuipuAuth(options);
  return new Configuration({
    basePath: options?.baseUrl ?? BASE_URL,
    headers: { Accept: "application/vnd.quipu.v1+json" },
    middleware: [auth],
  });
}

/**
 * Create all API instances with auto-refreshing OAuth2 auth.
 *
 * Usage:
 *   const client = createClient();
 *   const contacts = await client.contacts.getContacts();
 */
export function createClient(options?: {
  appId?: string;
  appSecret?: string;
  baseUrl?: string;
  scope?: string;
}) {
  const config = createConfig(options);
  return {
    accountingCategories: new apis.AccountingCategoriesApi(config),
    accountingSubcategories: new apis.AccountingSubcategoriesApi(config),
    attachments: new apis.AttachmentsApi(config),
    authentication: new apis.AuthenticationApi(config),
    bookEntries: new apis.BookEntriesApi(config),
    contacts: new apis.ContactsApi(config),
    invoices: new apis.InvoicesApi(config),
    numberingSeries: new apis.NumberingSeriesApi(config),
    paysheets: new apis.PaysheetsApi(config),
    tickets: new apis.TicketsApi(config),
  };
}

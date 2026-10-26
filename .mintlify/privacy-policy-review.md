# Privacy policy evidence and follow-up

Updated: 2026-10-26. Pages: `/privacy-policy`, `/ja/privacy-policy`, `/en/privacy-policy`.

## Confirmed by the user
- Operator: XrtoTech. This is the privacy notice operator identity; it does not change the help center branding.
- Privacy email: alam@xrtotech.com.
- No fixed retention period has been determined. All three notices disclose this; no deadline is invented.

## Source evidence
- `../../xiangou/prisma/schema.prisma`: authorization sessions, tokens and optional online administrator identity fields; only Session is modeled in this database.
- `../../xiangou/shopify.app.pro.toml`: scopes, compliance subscriptions and Shopify metafield declarations.
- `../../xiangou/app/routes/webhooks.orders_create.jsx` and `app/quantity-history.server.js`: incoming order payload, linked customer, product quantities and order time; Shopify customer metafield storage; processed order identifiers.
- `../../xiangou/extensions/*/src/cart_validations_generate_run.graphql`: cart, eligibility, tag matching, quantity, amount, weight and language inputs.
- `../../xiangou/app/routes/webhooks.app.uninstalled.jsx`: session cleanup conditional on a session; do not promise immediate deletion of all data.
- `../../xiangou/app/routes/webhooks.compliance.jsx`: shop redaction deletes remaining sessions; customer request/redaction topics currently acknowledge requests without additional export/delete logic. Do not claim a customer export or complete automatic erasure capability.
- `contact-widget.js`: optional WeChat contact. No analytics or cookie guarantees are inferred.

## Follow-up for the operator
- Determine category-specific retention and deletion rules for sessions, Shopify configuration/history, operational logs, backups and support communications.
- Confirm hosting/service providers, processing locations, international transfers and any applicable legal bases before adding related statements.
- No claims about data sales, advertising, comprehensive security certifications, guaranteed response times, or automatic deletion of all records are made.
- Mintlify Admin/Search MCP tools were not available in this session; changes were made in the local checkout, without publishing.

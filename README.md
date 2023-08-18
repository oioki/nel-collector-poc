# nel-collector-poc
Simple proxy-like NEL collector to Sentry

Add NEL headers to your site:

```
NEL: {"report_to":"nel","include_subdomains":true,"max_age":86400,"success_fraction": 0.0, "failure_fraction": 1.0}
Report-To: {"group":"nel","max_age":86400,"endpoints":[{"url":"https://your-nel-collector-endpoint/"}]}
```

and start the collector:

```
SENTRY_DSN="https://{{dsn_key}}@o{{your_org_id}}.ingest.sentry.io/{{your_project_id}}" ./collector.py
```

The collector will start listening for POST requests from the browsers, and send incoming events to Sentry
via `sentry_sdk.capture_message()`.

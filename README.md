# Sitting with Sissy

Landing page for Sitting with Sissy, an in-home house sitting and pet care service in Sacramento, CA.

Live site: https://sitting-with-sissy.vercel.app

## Files

- `sitting-with-sissy.html` is the page you edit.
- `img/` holds the photos (from Unsplash).
- `build-site.py` turns the page into a ready-to-host website in `site/`.
- `site/` is what gets uploaded to Vercel. Don't edit it by hand; rebuild it instead.

## Update the live site

```bash
python3 build-site.py
cd site
npx vercel@latest deploy --prod --yes
```

## Before launch

In the second `<script>` of `sitting-with-sissy.html`, the `CONFIG` block holds Sissy's phone number, email, social links, prices and the booking form endpoint (e.g. a Formspree URL). Replace the placeholders there, plus the sample reviews, service areas and cancellation policy.

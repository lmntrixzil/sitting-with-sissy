"""Build a standalone static site in ./site from sitting-with-sissy.html.

The source file is written for the Claude artifact viewer, which supplies the
<!doctype>, <html>, <head> and <body> wrapper. A normal host such as Vercel
needs that wrapper in the file itself, so this script adds it, plus a favicon
and share-preview tags, and copies the images.

Run:  python3 build-site.py
Then deploy the ./site folder.
"""
import pathlib
import shutil

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "sitting-with-sissy.html"
OUT = ROOT / "site"

DESCRIPTION = ("In-home house sitting and pet care in Sacramento, CA. Your pets stay home "
               "while Sissy handles walks, meals, plants, mail and daily photo updates.")

FAVICON = ("data:image/svg+xml,"
           "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E"
           "%3Cpath d='M6 22 L24 7 L42 22 V40 a4 4 0 0 1 -4 4 H10 a4 4 0 0 1 -4 -4 Z' fill='%23F7DA7B'/%3E"
           "%3Cpath d='M3 23 L24 5.5 L45 23' fill='none' stroke='%231F3349' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'/%3E"
           "%3Ccircle cx='18.5' cy='25' r='2.6' fill='%233A2E0E'/%3E%3Ccircle cx='24' cy='22.5' r='2.6' fill='%233A2E0E'/%3E"
           "%3Ccircle cx='29.5' cy='25' r='2.6' fill='%233A2E0E'/%3E"
           "%3Cpath d='M24 28.5c-4.5 0-7 4.2-7 6.6 0 2.4 2.2 3 3.6 3 1.4 0 2-.8 3.4-.8s2 .8 3.4.8c1.4 0 3.6-.6 3.6-3 0-2.4-2.5-6.6-7-6.6Z' fill='%233A2E0E'/%3E"
           "%3C/svg%3E")

EXTRA_HEAD = f"""<meta name="description" content="{DESCRIPTION}">
<meta name="theme-color" content="#D3E5F3">
<meta property="og:type" content="website">
<meta property="og:title" content="Sitting with Sissy · House & Pet Sitting in Sacramento">
<meta property="og:description" content="{DESCRIPTION}">
<link rel="icon" href="{FAVICON}">
"""


def main():
    src = SRC.read_text(encoding="utf-8")
    split_at = src.index("</style>") + len("</style>")
    head, body = src[:split_at], src[split_at:]
    page = ("<!doctype html>\n<html lang=\"en\">\n<head>\n" + head.strip() + "\n" + EXTRA_HEAD
            + "</head>\n<body>\n" + body.strip() + "\n</body>\n</html>\n")

    # Replace only the page and images, keeping Vercel's link files (.vercel/, .env.local, .gitignore)
    if (OUT / "img").exists():
        shutil.rmtree(OUT / "img")
    (OUT / "img").mkdir(parents=True)
    (OUT / "index.html").write_text(page, encoding="utf-8")
    for img in (ROOT / "img").glob("*.jpg"):
        shutil.copy2(img, OUT / "img" / img.name)
    print(f"Built {OUT / 'index.html'} with {len(list((OUT / 'img').iterdir()))} images")


if __name__ == "__main__":
    main()

import requests
import os
import time

SCHOLAR_ID = "ErU9OB4AAAAJ"
API_KEY = os.environ.get("SERPAPI_KEY")

print("API key loaded:", bool(API_KEY))

def serpapi_request(params):
    try:
        r = requests.get("https://serpapi.com/search", params=params, timeout=15)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"SerpAPI request failed: {e}")
        return None

def fetch_publications():
    params = {
        "engine": "google_scholar_author",
        "author_id": SCHOLAR_ID,
        "api_key": API_KEY,
        "num": "100"
    }

    print("Fetching publications…")
    data = serpapi_request(params)
    if not data:
        return []

    pubs = data.get("articles", [])
    print(f"Found {len(pubs)} publications")
    return pubs

def fetch_bibtex_from_title(title):
    params = {
        "engine": "google_scholar",
        "q": title,
        "api_key": API_KEY
    }

    data = serpapi_request(params)
    if not data:
        return None

    try:
        first_result = data["organic_results"][0]
        bibtex_url = first_result["inline_links"]["citation"]["bibtex"]
        bibtex = requests.get(bibtex_url, timeout=10).text.strip()
        return bibtex
    except Exception:
        return None

def main():
    if not API_KEY:
        print("ERROR: SERPAPI_KEY is not set.")
        return

    pubs = fetch_publications()
    bib_entries = []

    for pub in pubs:
        title = pub.get("title")
        if not title:
            continue

        print(f"Fetching BibTeX for: {title[:60]}…")
        bib = fetch_bibtex_from_title(title)

        if bib:
            bib_entries.append(bib)
        else:
            print(f"  → No BibTeX found for: {title}")

        time.sleep(1)

    with open("publications.bib", "w") as f:
        for entry in bib_entries:
            f.write(entry + "\n\n")

    print(f"Saved {len(bib_entries)} entries to publications.bib")

if __name__ == "__main__":
    main()

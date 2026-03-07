import requests
import os
import time

SCHOLAR_ID = "ErU9OB4AAAAJ"
API_KEY = os.environ["SERPAPI_KEY"]

def fetch_publications():
    """Fetch list of publications from the author profile."""
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_scholar_author",
        "author_id": SCHOLAR_ID,
        "api_key": API_KEY,
        "num": "100"
    }

    print("Fetching publications from SerpAPI…")
    data = requests.get(url, params=params).json()

    pubs = data.get("articles", [])
    print(f"Found {len(pubs)} publications")

    return pubs

def fetch_bibtex_from_article(citation_id):
    """Fetch BibTeX by loading the article page and extracting the BibTeX link."""
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_scholar",
        "q": f"citation_id:{citation_id}",
        "api_key": API_KEY
    }

    data = requests.get(url, params=params).json()

    # SerpAPI returns citation formats under "inline_links"
    try:
        bibtex_url = data["inline_links"]["citation"]["bibtex"]
        bibtex = requests.get(bibtex_url).text.strip()
        return bibtex
    except Exception:
        return None

def main():
    pubs = fetch_publications()
    bib_entries = []

    for pub in pubs:
        citation_id = pub.get("citation_id")
        if not citation_id:
            continue

        print(f"Fetching BibTeX for {citation_id}…")
        bib = fetch_bibtex_from_article(citation_id)

        if bib:
            bib_entries.append(bib)
        else:
            print(f"  → No BibTeX found for {citation_id}")

        time.sleep(1)  # be polite to the API

    with open("publications.bib", "w") as f:
        for entry in bib_entries:
            f.write(entry + "\n\n")

    print(f"Saved {len(bib_entries)} BibTeX entries to publications.bib")

if __name__ == "__main__":
    main()

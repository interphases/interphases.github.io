import requests
import os
import time

SCHOLAR_ID = "ErU9OB4AAAAJ"
API_KEY = os.environ["SERPAPI_KEY"]

def fetch_publications():
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_scholar_author",
        "author_id": SCHOLAR_ID,
        "api_key": API_KEY,
        "num": "100"
    }

    print("Fetching publications from SerpAPI…")
    data = requests.get(url, params=params, timeout=20).json()

    pubs = data.get("articles", [])
    print(f"Found {len(pubs)} publications")

    return pubs

def fetch_bibtex(citation_id):
    """Fetch BibTeX using the official google_scholar_cite engine."""
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_scholar_cite",
        "q": citation_id,
        "api_key": API_KEY
    }

    data = requests.get(url, params=params, timeout=20).json()

    try:
        formats = data["citations"]
        for fmt in formats:
            if fmt["title"].lower() == "bibtex":
                return fmt["snippet"]
    except Exception:
        return None

    return None

def main():
    pubs = fetch_publications()
    bib_entries = []

    for pub in pubs:
        citation_id = pub.get("citation_id")
        if not citation_id:
            continue

        print(f"Fetching BibTeX for {citation_id}…")
        bib = fetch_bibtex(citation_id)

        if bib:
            bib_entries.append(bib)
        else:
            print(f"  → No BibTeX found for {citation_id}")

        time.sleep(1)  # avoid rate limits

    with open("publications.bib", "w") as f:
        for entry in bib_entries:
            f.write(entry + "\n\n")

    print(f"Saved {len(bib_entries)} BibTeX entries to publications.bib")

if __name__ == "__main__":
    main()

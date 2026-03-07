import requests
import os
import time

SCHOLAR_ID = "ErU9OB4AAAAJ"
API_KEY = os.environ["SERPAPI_KEY"]

def serpapi_request(params):
    """Wrapper with timeout and error handling."""
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

def fetch_bibtex_from_url(url):
    """Fetch BibTeX directly from the citation link."""
    try:
        r = requests.get(url, timeout=10)
        return r.text.strip()
    except Exception as e:
        print(f"Failed to fetch BibTeX: {e}")
        return None

def fetch_bibtex(citation_id):
    """Use google_scholar_cite to get citation formats."""
    params = {
        "engine": "google_scholar_cite",
        "q": citation_id,
        "api_key": API_KEY
    }

    data = serpapi_request(params)
    if not data:
        return None

    try:
        for item in data.get("citations", []):
            if item["title"].lower() == "bibtex":
                return item["snippet"]
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

    print(f"Saved {len(bib_entries)} entries to publications.bib")

if __name__ == "__main__":
    main()

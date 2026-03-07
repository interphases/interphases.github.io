import requests
import os

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
    data = requests.get(url, params=params).json()

    pubs = data.get("articles", [])
    print(f"Found {len(pubs)} publications")

    return pubs

def fetch_bibtex(citation_url):
    """Fetch BibTeX using the citation link provided by SerpAPI."""
    r = requests.get(citation_url)
    return r.text.strip()

def main():
    pubs = fetch_publications()

    bib_entries = []

    for pub in pubs:
        citation = pub.get("citation")
        if not citation:
            continue

        bibtex_url = citation.get("bibtex")
        if not bibtex_url:
            continue

        try:
            bib = fetch_bibtex(bibtex_url)
            bib_entries.append(bib)
        except Exception as e:
            print(f"Failed to fetch BibTeX: {e}")

    with open("publications.bib", "w") as f:
        for entry in bib_entries:
            f.write(entry + "\n\n")

    print(f"Saved {len(bib_entries)} BibTeX entries to publications.bib")

if __name__ == "__main__":
    main()

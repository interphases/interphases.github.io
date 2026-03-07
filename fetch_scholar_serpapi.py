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
        "num": "100"  # fetch up to 100 publications
    }

    print("Fetching publications from SerpAPI…")
    data = requests.get(url, params=params).json()

    pubs = data.get("articles", [])
    print(f"Found {len(pubs)} publications")

    return pubs

def fetch_bibtex(pub_id):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_scholar_bibtex",
        "q": pub_id,
        "api_key": API_KEY
    }
    r = requests.get(url, params=params)
    return r.text.strip()

def main():
    pubs = fetch_publications()

    bib_entries = []
    for pub in pubs:
        pub_id = pub.get("citation_id")
        if not pub_id:
            continue
        try:
            bib = fetch_bibtex(pub_id)
            bib_entries.append(bib)
        except Exception as e:
            print(f"Failed to fetch BibTeX for {pub_id}: {e}")

    with open("publications.bib", "w") as f:
        for entry in bib_entries:
            f.write(entry + "\n\n")

    print(f"Saved {len(bib_entries)} BibTeX entries to publications.bib")

if __name__ == "__main__":
    main()

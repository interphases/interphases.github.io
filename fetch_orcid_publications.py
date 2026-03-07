import requests
import time
import bibtexparser

ORCID = "0000-0001-5653-0383"

def fetch_orcid_works(orcid):
    url = f"https://pub.orcid.org/v3.0/{orcid}/works"
    headers = {"Accept": "application/json"}
    r = requests.get(url, headers=headers, timeout=20)
    r.raise_for_status()
    return r.json()

def fetch_crossref_metadata(doi):
    url = f"https://api.crossref.org/works/{doi}"
    r = requests.get(url, timeout=20)
    if r.status_code != 200:
        return None
    return r.json()["message"]

def crossref_to_bibtex(meta):
    # Safe helpers
    def safe_get_list(meta, key):
        val = meta.get(key, [])
        return val[0] if isinstance(val, list) and val else ""

    def safe_get_year(meta):
        try:
            return meta.get("issued", {}).get("date-parts", [[None]])[0][0]
        except Exception:
            return ""

    entry = {
        "ENTRYTYPE": meta.get("type", "article"),
        "ID": meta.get("DOI", "unknown").replace("/", "_"),
        "title": safe_get_list(meta, "title"),
        "year": safe_get_year(meta),
        "doi": meta.get("DOI", ""),
        "journal": safe_get_list(meta, "container-title"),
    }

    # Authors
    authors = []
    for a in meta.get("author", []):
        parts = []
        if "given" in a:
            parts.append(a["given"])
        if "family" in a:
            parts.append(a["family"])
        if parts:
            authors.append(" ".join(parts))
    entry["author"] = " and ".join(authors)

    return entry

def main():
    print("Fetching ORCID works…")
    works = fetch_orcid_works(ORCID)

    bib_database = bibtexparser.bibdatabase.BibDatabase()
    bib_entries = []

    for group in works.get("group", []):
        summary = group["work-summary"][0]

        # Extract DOI
        doi = None
        for ext in summary.get("external-ids", {}).get("external-id", []):
            if ext["external-id-type"].lower() == "doi":
                doi = ext["external-id-value"]
                break

        if not doi:
            print("No DOI found, skipping entry")
            continue

        print(f"Fetching Crossref metadata for DOI: {doi}")
        meta = fetch_crossref_metadata(doi)
        if not meta:
            print("  → No Crossref metadata found")
            continue

        bib_entry = crossref_to_bibtex(meta)
        bib_entries.append(bib_entry)

        time.sleep(1)  # polite rate limiting

    bib_database.entries = bib_entries

    with open("publications.bib", "w") as f:
        bibtexparser.dump(bib_database, f)

    print(f"Saved {len(bib_entries)} entries to publications.bib")

if __name__ == "__main__":
    main()

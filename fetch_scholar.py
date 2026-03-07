from scholarly import scholarly

SCHOLAR_ID = "ErU9OB4AAAAJ"   # <-- replace this

def main():
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["publications"])

    bib_entries = []

    for pub in author["publications"]:
        filled = scholarly.fill(pub)
        bibtex = filled.get("bibtex")
        if bibtex:
            bib_entries.append(bibtex)

    with open("publications.bib", "w") as f:
        for entry in bib_entries:
            f.write(entry + "\n\n")

if __name__ == "__main__":
    main()

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogenize_latex_encoding

def acs_format(entry):
    """Format a BibTeX entry in ACS style."""
    authors = entry.get("author", "").split(" and ")
    authors_formatted = ", ".join(authors)

    title = entry.get("title", "")
    journal = entry.get("journal", "")
    year = entry.get("year", "")
    doi = entry.get("doi", "")

    parts = [
        f"**{authors_formatted}**.",
        f"*{title}*.",
        f"_{journal}_",
        f"**{year}**.",
    ]

    if doi:
        parts.append(f"[DOI: {doi}](https://doi.org/{doi})")

    return " ".join(parts)

def main():
    with open("publications.bib") as bibtex_file:
        parser = BibTexParser()
        parser.customization = homogenize_latex_encoding
        bib = bibtexparser.load(bibtex_file, parser=parser)

    # Sort by year descending
    entries = sorted(
        bib.entries,
        key=lambda x: x.get("year", "0"),
        reverse=True
    )

    lines = ["# Publications\n"]

    for entry in entries:
        lines.append(f"- {acs_format(entry)}")

    with open("publications.md", "w") as f:
        f.write("\n".join(lines))

    print("Updated publications.md")

if __name__ == "__main__":
    main()

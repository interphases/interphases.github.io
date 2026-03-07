import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogenize_latex_encoding

def acs_format(entry):
    authors = entry.get("author", "").split(" and ")
    authors_formatted = ", ".join(authors)

    title = entry.get("title", "")
    journal = entry.get("journal", "")
    year = entry.get("year", "")
    doi = entry.get("doi", "")

    parts = [
        f"**{authors_formatted}**.",
        f"*{title}*.",
    ]

    if journal:
        parts.append(f"_{journal}_")

    if year:
        parts.append(f"**{year}**.")

    if doi:
        parts.append(f"[DOI: {doi}](https://doi.org/{doi})")

    return " ".join(parts)

def main():
    with open("publications.bib") as bibtex_file:
        parser = BibTexParser(common_strings=True)
        parser.customization = homogenize_latex_encoding
        parser.ignore_nonstandard_types = False  # ← this is the important line
        bib = bibtexparser.load(bibtex_file, parser=parser)

    entries = sorted(
        bib.entries,
        key=lambda x: str(x.get("year", "0")),
        reverse=True,
    )

    lines = ["# Publications", ""]

    for entry in entries:
        lines.append(f"- {acs_format(entry)}")

    with open("publications.md", "w") as f:
        f.write("\n".join(lines))

    print(f"Updated publications.md with {len(entries)} entries")

if __name__ == "__main__":
    main()

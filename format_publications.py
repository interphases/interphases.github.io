from pybtex.database import parse_file

def acs_format(entry):
    authors = []
    for person in entry.persons.get("author", []):
        authors.append(" ".join(person.first_names + person.last_names))

    authors_formatted = ", ".join(authors)

    title = entry.fields.get("title", "")
    journal = entry.fields.get("journal", "")
    year = entry.fields.get("year", "")
    doi = entry.fields.get("doi", "")

    parts = []

    if authors_formatted:
        parts.append(f"**{authors_formatted}**.")

    if title:
        parts.append(f"*{title}*.")

    if journal:
        parts.append(f"_{journal}_")

    if year:
        parts.append(f"**{year}**.")

    if doi:
        parts.append(f"[DOI: {doi}](https://doi.org/{doi})")

    return " ".join(parts)

def main():
    bib = parse_file("publications.bib")

    # Flatten entries
    entries = list(bib.entries.values())

    # Sort by year descending
    entries.sort(key=lambda e: e.fields.get("year", "0"), reverse=True)

    lines = ["# Publications", ""]

    for entry in entries:
        lines.append(f"- {acs_format(entry)}")

    with open("publications.md", "w") as f:
        f.write("\n".join(lines))

    print(f"Updated publications.md with {len(entries)} entries")

if __name__ == "__main__":
    main()

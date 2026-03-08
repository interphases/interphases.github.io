from pybtex.database import parse_file

# ---------------------------------------------------------------------
# Journal abbreviation dictionary (extend as needed)
# ---------------------------------------------------------------------
JOURNAL_ABBREVIATIONS = {
    "Journal of the American Chemical Society": "J. Am. Chem. Soc.",
    "Chemistry of Materials": "Chem. Mater.",
    "Journal of Power Sources": "J. Power Sources",
    "Advanced Materials": "Adv. Mater.",
    "Advanced Energy Materials": "Adv. Energy Mater.",
    "Advanced Functional Materials": "Adv. Funct. Mater.",
    "Small": "Small",
    "Nature Communications": "Nat. Commun.",
    "Nature Energy": "Nat. Energy",
    "Nature Materials": "Nat. Mater.",
    "Scientific Reports": "Sci. Rep.",
    "Electrochimica Acta": "Electrochim. Acta",
    "Journal of Physical Chemistry C": "J. Phys. Chem. C",
    "Journal of Physical Chemistry Letters": "J. Phys. Chem. Lett.",
    "ACS Energy Letters": "ACS Energy Lett.",
    "ACS Applied Materials & Interfaces": "ACS Appl. Mater. Interfaces",
    "ACS Materials Letters": "ACS Mater. Lett.",
    "ChemSusChem": "ChemSusChem",
    "ChemElectroChem": "ChemElectroChem",
    "Energy & Environmental Science": "Energy Environ. Sci.",
    "Journal of The Electrochemical Society": "J. Electrochem. Soc.",
    "Carbon": "Carbon",
    "Chemical Engineering Journal": "Chem. Eng. J.",
    "Frontiers in Energy Research": "Front. Energy Res.",
    "Electrochemistry": "Electrochemistry",
    "Green": "Green",
    "Journal of Pharmaceutical Sciences": "J. Pharm. Sci.",
}

# ---------------------------------------------------------------------
# Icons
# ---------------------------------------------------------------------
ICON_ORCID = "🟢"
ICON_DOI = "🔗"
ICON_CROSSREF = "📘"

# ---------------------------------------------------------------------
# ACS-style formatter
# ---------------------------------------------------------------------
def acs_format(entry):
    """Format a BibTeX entry in ACS style with icons and abbreviations."""

    # --- Authors --------------------------------------------------------------
    authors = []
    for person in entry.persons.get("author", []):
        full = " ".join(person.first_names + person.last_names)
        authors.append(full)
    authors_formatted = ", ".join(authors)

    # --- Fields ---------------------------------------------------------------
    title = entry.fields.get("title", "")
    journal = entry.fields.get("journal", "")
    year = entry.fields.get("year", "")
    volume = entry.fields.get("volume", "")
    number = entry.fields.get("number", "")
    pages = entry.fields.get("pages", "")
    doi = entry.fields.get("doi", "")

    # --- Journal abbreviation -------------------------------------------------
    journal_abbrev = JOURNAL_ABBREVIATIONS.get(journal, journal)

    # --- Pages / Article number ----------------------------------------------
    page_part = pages

    # --- Build ACS-style entry ------------------------------------------------
    parts = []

    if authors_formatted:
        parts.append(f"**{authors_formatted}**.")

    if title:
        parts.append(f"*{title}*.")

    if journal_abbrev:
        parts.append(f"_{journal_abbrev}_")

    # Volume (bold), issue in parentheses
    if volume:
        vol_str = f"**{volume}**"
        if number:
            vol_str += f"({number})"
        parts.append(vol_str + ",")

    # Pages or article number
    if page_part:
        parts.append(page_part + ",")

    # Year
    if year:
        parts.append(f"**{year}**.")

    # DOI link with icons
    if doi:
        parts.append(f"{ICON_DOI} [DOI: {doi}](https://doi.org/{doi}) {ICON_CROSSREF}")

    return " ".join(parts)


# ---------------------------------------------------------------------
# Main script
# ---------------------------------------------------------------------
def main():
    bib = parse_file("publications.bib")

    # Flatten entries
    entries = list(bib.entries.values())

    # Filter: only 2016 and later
    entries = [
        e for e in entries
        if e.fields.get("year") and int(e.fields["year"]) >= 2016
    ]

    # Sort by year descending
    entries.sort(key=lambda e: e.fields.get("year", "0"), reverse=True)

    lines = ["# Publications", ""]

    for entry in entries:
        lines.append(f"- {acs_format(entry)}")

    with open("publications.md", "w") as f:
        f.write("\n".join(lines))

    print(f"Updated publications.md with {len(entries)} entries (2016 and later)")


if __name__ == "__main__":
    main()

from scholarly import scholarly
import signal

SCHOLAR_ID = "ErU9OB4AAAAJ"

# Timeout handler
class TimeoutException(Exception):
    pass

def timeout(seconds=10):
    def decorator(func):
        def wrapper(*args, **kwargs):
            def handler(signum, frame):
                raise TimeoutException()
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)
        return wrapper
    return decorator

@timeout(10)
def safe_fill(pub):
    return scholarly.fill(pub)

def main():
    print(f"Fetching publications for Google Scholar ID: {SCHOLAR_ID}")

    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["publications"])

    bib_entries = []

    for pub in author["publications"]:
        try:
            filled = safe_fill(pub)
            bibtex = filled.get("bibtex")
            if bibtex:
                bib_entries.append(bibtex)
        except TimeoutException:
            print("Timeout on publication, skipping.")
        except Exception as e:
            print(f"Error fetching publication: {e}")

    with open("publications.bib", "w") as f:
        for entry in bib_entries:
            f.write(entry + "\n\n")

    print(f"Saved {len(bib_entries)} publications to publications.bib")

if __name__ == "__main__":
    main()

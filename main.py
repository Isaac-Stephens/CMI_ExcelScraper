from pathlib import Path
from scraper import unzip_workbooks_recursive, extract_docs

INPUT_DIR = Path("sheets")
UNZIPPED_DIR = Path("unzipped")
EXTRACTED_DOC_DIR = Path("extracted_docs")
INVALID_UNZIPPED_DIR = Path(UNZIPPED_DIR / "invalid")
INVALID_EXTRACTED_DIR = Path(EXTRACTED_DOC_DIR / "invalid")

if __name__ == "__main__":
    unzip_workbooks_recursive(INPUT_DIR, UNZIPPED_DIR)
    extract_docs(UNZIPPED_DIR, EXTRACTED_DOC_DIR)
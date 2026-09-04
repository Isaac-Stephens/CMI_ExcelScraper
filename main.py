from pathlib import Path
from scraper import unzip_workbooks, extract_docs

INPUT_DIR = Path("sheets")
UNZIPPED_DIR = Path("unzipped")
EXTRACTED_DOC_DIR = Path("extracted_docs")

if __name__ == "__main__":
    unzip_workbooks(INPUT_DIR, UNZIPPED_DIR)
    extract_docs(UNZIPPED_DIR, EXTRACTED_DOC_DIR)
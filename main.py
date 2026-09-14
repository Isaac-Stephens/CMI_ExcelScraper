from pathlib import Path
from scraper import unzip_workbooks_recursive, extract_docs, organize_docs

INPUT_DIR = Path("sheets")
UNZIPPED_DIR = Path("unzipped")
EXTRACTED_DOC_DIR = Path("extracted_docs")
ORGANIZED_DOCS_DIR = Path("organized_docs")

if __name__ == "__main__":
    unzip_workbooks_recursive(INPUT_DIR, UNZIPPED_DIR)
    extract_docs(UNZIPPED_DIR, EXTRACTED_DOC_DIR)
    organize_docs(EXTRACTED_DOC_DIR, ORGANIZED_DOCS_DIR)
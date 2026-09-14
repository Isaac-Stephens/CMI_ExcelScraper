from pathlib import Path
from zipfile import ZipFile
import shutil
import re


# Unzips all .xlsx workbooks from input_dir and exports to output_dir
def unzip_workbooks(input_dir: Path, output_dir: Path):
    output_dir.mkdir(exist_ok=True)

    for workbook in input_dir.glob("*.xlsx"):
        workbook_output = output_dir / workbook.stem
        workbook_output.mkdir(exist_ok=True)

        print(f"Extracting: {workbook}")

        with ZipFile(workbook, "r") as zip_file:
            zip_file.extractall(workbook_output)

        print(f" -> {workbook_output}")

# Renames docs from input_dir/[name]/xl/embedding/*.docx to [name]_[increment].docx and moves them to output_dir
def extract_docs(input_dir: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    for workbook_dir in input_dir.iterdir():
        if not workbook_dir.is_dir():
            continue

        embeddings_dir = workbook_dir / "xl" / "embeddings"

        # skip if no embeddings dir
        if not embeddings_dir.exists():
            print(f"No embeddings directory: {workbook_dir.name}")
            continue

        word_files = sorted(
            embeddings_dir.glob("Microsoft_Word_Document*.docx")
        )

        for file_number, word_file in enumerate(word_files, start=1):
            new_name = f"{workbook_dir.name}_{file_number}.docx"
            destination = output_dir / new_name

            # print(f"Moving: {word_file}")
            # print(f"    -> {destination}")

            shutil.move(word_file, destination)

def unzip_workbooks_recursive(input_dir: Path, output_dir: Path):
    output_dir.mkdir(exist_ok=True)

    # find every .xlsx file under input_dir
    for workbook in input_dir.rglob("*.xlsx"):
        filename = workbook.stem # get the file name as a string

        # parse, return true if matches naming conventions
        match = re.match(
            r"^"
            r"(\d{1,3})[._\s]+" # FA
            r"(\d{1,3})[._\s]+" # ID1
            r"(\d{1,3})[._\s]+" # ID2
            r"(.+?)"            # Researcher
            r"[_\s-]*"          # Spacing
            r"[Yy][Rr]\s*(\d{1,2})" # Year
            r"[_\s-]*"
            r"[Qq]\s*(\d+)",    # Quarter
            filename
        )

        # extract all invalid named workbooks to unzipped/invalid
        if not match:
            print(f"Invalid filename: {workbook}")
            continue

        # separate components
        fa_id, id1, id2, researcher, year, quarter = match.groups()

        year = year.zfill(2)

        directory_name = (
            f"{researcher}_{fa_id}-{id1}-{id2}_YR{year}_Q{quarter}"
        )

        workbook_output = output_dir / directory_name

        # handle duplicate workbooks
        if workbook_output.exists():
            duplicate_number = 1

            while True:
                duplicate_name = f"{directory_name}({duplicate_number})"
                duplicate_output = output_dir / duplicate_name

                if not duplicate_output.exists():
                    workbook_output = duplicate_output
                    print(
                        f"Duplicate output directory: "
                        f"{output_dir / directory_name}"
                    )
                    break

                duplicate_number += 1

        # print(f"Extracting: {workbook}")
        # print(f" -> {workbook_output}")

        workbook_output.mkdir(parents=True, exist_ok=False)

        with ZipFile(workbook, "r") as zip_file:
            zip_file.extractall(workbook_output)

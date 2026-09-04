from pathlib import Path
from zipfile import ZipFile
import shutil


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

            print(f"Moving: {word_file}")
            print(f"    -> {destination}")

            shutil.move(word_file, destination)
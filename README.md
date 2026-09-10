# Simple Excel Scraper

Takes an input directory, finds all the .xlsx files, and extracts all the embedded word documents to a separate directory.

Built as a tool for the Critical Materials Innovation Hub.

## Set Up

#### Linux (Debian based)

PRE: Install Python 3 and Git
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 pip3 git
```
1) Clone and navigate to this repository
```bash
git clone https://github.com/Isaac-Stephens/CMI_ExcelScraper.git
cd CMI_ExcelScraper
```
2) Create a venv environment for python and install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install pathlib
```
3) Create input directory and upload your sheets here.
```bash
mkdir sheets
```
4) Run the program
```bash
python3 main.py
```
5) All extracted sheets should be in a directory called "extracted_docs"!

#### Windows

PRE: Install Python 3 and Git

1) Clone and navigate to this repository.

Open **PowerShell** and run:
``` bash
git clone https://github.com/Isaac-Stephens/CMI_ExcelScraper.git
cd CMI_ExcelScraper
```

2) Create a venv environment for python and install dependencies

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
> If PowerShell prevents this activation, you may need to allow locally created scripts:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

> Then activate the environment again:
```bash
.\.venv\Scripts\Activate.ps1
```

3) Create the input folder and upload your Excel sheets here.
```bash
mkdir sheets
```
Place all the `.xlsx` files you want to process insisde the `sheets` folder.

4) Run the program
```bash
python3 main.py
```

5) All extracted sheets should be in a folder called "extracted_docs"!


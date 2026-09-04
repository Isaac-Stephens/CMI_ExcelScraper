# Simple Excel Scraper

Takes an input directory, finds all the .xlsx files, and extracts all the embedded word documents to a separate directory.

Built as a tool for the Critical Materials Innovation Hub.

## Set Up

#### Linux (Debian based)

PRE: Install python.
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 pip3
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
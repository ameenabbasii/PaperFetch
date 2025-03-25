# cie_pastpaperdownloader
This repository contains a Python script that downloads past papers and marking schemes from PapaCambridge, merges them into a single PDF, and allows users to choose where to save the files.

⸻

1. **Features**
	•	Downloads past papers and marking schemes for CAIE exams
	•	Merges question papers and marking schemes into a single PDF
	•	Allows users to choose directories for saving files
	•	Handles network errors and missing files gracefully
	•	Converts into an executable.exe for easy use

2. **Installation**

Step 1: Clone the Repository
```
git clone https://github.com/ameenabbasii/cie_pastpaperdownloader.git
cd cie_pastpaperdownloader
```
Step 2: Convert to Executable (.exe)
   
For Windows users, you can create an executable:
```
pyinstaller --onefile --windowed --icon=icon.ico pdf_downloader.py
```

To install dependencies from this file, run:
```
pip install -r requirements.txt
```

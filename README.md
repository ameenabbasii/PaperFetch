# ***PaperFetch***
This is a python script which, when given the subject-code & variant, installs all the relevant past-papers for that subject and stores in a specified file.

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
git clone https://github.com/ameenabbasii/PaperFetch.git
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

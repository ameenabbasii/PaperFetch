import os
import sys
import requests
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter

root = tk.Tk()
root.withdraw()




folder_pdf_qp = filedialog.askdirectory(title="Select folder for Question Papers ")
folder_pdf_ms = filedialog.askdirectory(title="Select folder for Marking Schemes")
folder_pdf_pp = filedialog.askdirectory(title="Select folder for Merged PDFs")

if not folder_pdf_qp or not folder_pdf_ms or not folder_pdf_pp:
    sys.exit("Error: You must select directories for saving files.")

try:
    user_input_subject = int(input("Enter a subject code: "))
    user_input_variant = int(input("Enter paper and variant (e.g., 12): "))
    
except ValueError:
    sys.exit("Invalid input. Please enter valid numeric values.")

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    try:
        with open(pdf1_path, 'rb') as file1, open(pdf2_path, 'rb') as file2:
            reader1 = PdfReader(file1)
            reader2 = PdfReader(file2)
            writer = PdfWriter()
            
            for page in reader1.pages:
                writer.add_page(page)
            for page in reader2.pages:
                writer.add_page(page)

            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

        print(f"PDFs merged successfully: {output_path}")

    except Exception as e:
        print(f"Error merging PDFs:{e}")

for i in range(10, 24):
    try:
        url_qp = f"https://pastpapers.papacambridge.com/directories/CAIE/CAIE-pastpapers/upload/{user_input_subject}_w{i}_qp_{user_input_variant}.pdf"
        response_qp = requests.get(url_qp, timeout=10)
        response_qp.raise_for_status()

        qp_path = os.path.join(folder_pdf_qp, f"{user_input_subject}_w{i}_qp_{user_input_variant}.pdf")
        with open(qp_path, 'wb') as pdf_qp:
            pdf_qp.write(response_qp.content)
        print(f"Downloaded: {qp_path}")

    except requests.RequestException as e:
        print(f"Failed to download Question Paper. Error: {e}")
        continue  

    try:
        url_ms = f"https://pastpapers.papacambridge.com/directories/CAIE/CAIE-pastpapers/upload/{user_input_subject}_w{i}_ms_{user_input_variant}.pdf"
        response_ms = requests.get(url_ms, timeout=10)
        response_ms.raise_for_status()

        ms_path = os.path.join(folder_pdf_ms, f"{user_input_subject}_w{i}_ms_{user_input_variant}.pdf")
        with open(ms_path, 'wb') as pdf_ms:
            pdf_ms.write(response_ms.content)
        print(f"Downloaded: {ms_path}")

    except requests.RequestException as e:
        print(f"Failed to download Marking Scheme. Error: {e}")
        continue  

    output_path = os.path.join(folder_pdf_pp, f"merged_file_{user_input_subject}_w{i}_{user_input_variant}.pdf")
    merge_pdfs(qp_path, ms_path, output_path)

print("Download and merge completed successfully.")
input("Press ENTER to exit.")

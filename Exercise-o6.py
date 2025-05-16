from PyPDF2 import PdfWriter
import os
merger = PdfWriter()

pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in pdf_files:
    merger.append(pdf)

output_filename = "merged-pdf.pdf"
merger.write(output_filename)
merger.close()

print(f"Merged PDF saved as {output_filename}")

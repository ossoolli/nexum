import sys
import os
from PyPDF2 import PdfReader

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = "".join([page.extract_text() for page in reader.pages])
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = f"shared_memory/extracted_texts/{base_name}.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"تم استخراج النص إلى: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        extract_text(sys.argv[1])

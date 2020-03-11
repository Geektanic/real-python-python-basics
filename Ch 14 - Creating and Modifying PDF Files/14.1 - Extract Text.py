# 14.1 Extract Text.py

from pathlib import Path
from PyPDF2 import PdfFileReader

pdf_path = (
    Path.home() /
    "Documents" /
    "Pride_and_Prejudice.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))
output_file = Path.home() / "Documents" / "Pride_and_Predjudice.txt"

with output_file.open(mode = "w") as output_file:
    output_file.write(
        f"{pdf_reader.documentInfo.title}\n"
        f"Number of pages: {pdf_reader.getNumPages()}\n\n"
    )

    for page in pdf_reader.pages:
        text = page.extractText()
        output_file.write(text)
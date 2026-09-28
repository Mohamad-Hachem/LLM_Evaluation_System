from pymupdf import open
import re
from typing import List
from pathlib import Path



def extract_paragraphs(pdf_path: str | Path) -> List[str]:
    """This function takes a pdf and return an array of paragraphs"""
    doc = open(pdf_path)
    paragraphs = []

    for page in doc:
        # get blocks from the page
        blocks = page.get_text("blocks")

        # Sort blocks from top to bottom
        blocks = sorted(blocks, key=lambda b: (b[1], b[0]))

        for block in blocks:
            text = block[4]

            # Replace line breaks inside a paragraph with spaces
            text = re.sub(r"\r+", " ",text).strip()

            if text:
                paragraphs.append(text)

    return paragraphs

"""
paragraphs = extract_paragraphs("pdfs/Penguins_ACL.pdf")\

for i, paragraph in enumerate(paragraphs, 1):
    print(f"pragraph {i}")
    print(paragraph)
    print()
"""


from pymupdf import open
import re
from typing import List
from pathlib import Path

def extract_paragraphs(pdf_path: str | Path) -> List[str]:
    """this function takes a pdf path and return an array of its paragraphs"""
    doc = open(pdf_path)
    paragraphs = []

    for page in doc:
        # get blocks from the page
        blocks = page.get_text("blocks")

        # sort blocks from top to bottom
        blocks = sorted(blocks, key=lambda b:(b[1], b[0]))

        for block in blocks:
            text = block[4]

            # Replace line breaks inside a paragraph with spaces
            text = re.sub(r"\r+", " ", text).strip()

            if text:
                paragraphs.append(text)

    return paragraphs

#print(len(extract_paragraphs("../pdfs/Penguins_ACL.pdf")))
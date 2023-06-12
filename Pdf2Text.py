#! /usr/bin/env python3

from PyPDF2 import PdfReader
import sys

def extractTextFromPdf(pdfPath):
    # creating a pdf reader object
    reader = PdfReader(pdfPath)
    
    # printing number of pages in pdf file
    print(len(reader.pages))
    
    # getting a specific page from the pdf file
    # page = reader.pages[0]
    
    # extracting text from page
    # text = page.extract_text()
    # print(text)
    with open(pdfPath[:-4] + "-extracted-text.txt", "w+", encoding="UTF-8") as output:
        for page in reader.pages:
            text = page.extract_text()
            output.write(text)

def main():
    extractTextFromPdf(sys.argv[1])

if __name__ == "__main__":
    main()
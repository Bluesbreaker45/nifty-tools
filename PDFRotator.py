import PyPDF2
import sys

def rotate(path):
    pdfIn = open(path, 'rb') # exchange the 'original.pdf' with a name of your file 
    pdfReader = PyPDF2.PdfReader(pdfIn)
    pdfWriter = PyPDF2.PdfWriter()

    for pageNum in range(len(pdfReader.pages)):
        page = pdfReader.pages[pageNum]
        page.rotate(90)
        pdfWriter.add_page(page)

    pdfOut = open('rotated.pdf', 'wb')
    pdfWriter.write(pdfOut)
    pdfOut.close()
    pdfIn.close()

def main():
    rotate(sys.argv[1])

if __name__ == "__main__":
    main()
import PyPDF2
import sys

def rotate(path):
    pdfIn = open(path, 'rb') # exchange the 'original.pdf' with a name of your file 
    pdfReader = PyPDF2.PdfFileReader(pdfIn)
    pdfWriter = PyPDF2.PdfFileWriter()

    for pageNum in range(pdfReader.numPages):
        page = pdfReader.getPage(pageNum)
        page.rotateClockwise(90)
        pdfWriter.addPage(page)

    pdfOut = open('rotated.pdf', 'wb')
    pdfWriter.write(pdfOut)
    pdfOut.close()
    pdfIn.close()

def main():
    rotate(sys.argv[1])

if __name__ == "__main__":
    main()
import os
import re
import argparse
from PyPDF2 import PdfMerger

def mergePdfs(directory, resultName):
  def extract_name(name):
    f = filter(lambda x: True if x else False, re.split("([0-9]+)|([^0-9]+)", name))
    m = map(lambda x: int(x) if x.isdigit() else x, f)
    return list(m)

  pdfs = filter(lambda x: x.endswith((".pdf")) and x != resultName, os.listdir(directory))
  pdfs = sorted(pdfs, key=extract_name)

  # If you want to control the order manually, specify it in the following list:
  # pdfs = [
  #   "1.pdf",
  #   "2.pdf"
  # ]

  print(len(pdfs))
  print(pdfs)

  if directory[-1] != '/':
    directory += '/'

  merger = PdfMerger()
  for pdf in pdfs:
    merger.append(directory + pdf)
  merger.write(resultName)
  merger.close()

def main():
  parser = argparse.ArgumentParser(description="Merge multiple pdfs.")
  parser.add_argument("-d", dest="dir", metavar="src_directory", default=".", help="path to source pdfs' directory (default: current working directory \".\")")
  parser.add_argument("-o", dest="newName", metavar="output's_name", default="merged.pdf", help="the name of the output pdf (default: \"merged.pdf\")")

  args = parser.parse_args()

  mergePdfs(args.dir, args.newName)

if __name__ == "__main__":
  main()

import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_merger(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		merger.append(pdf)
	merger.write("superPDF.pdf")

pdf_merger(inputs)
print()
print("---------------Your PDF files have been merged into one PDF File.Thanks for using the tool-------------------")
print()



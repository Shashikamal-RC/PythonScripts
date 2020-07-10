import PyPDF2
import sys

input = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('./pdfs/super.pdf')


pdf_combiner(input)

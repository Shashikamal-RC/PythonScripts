import PyPDF2

with open("./pdfs/two_pages.pdf", 'rb') as file:
    reader = PyPDF2.PdfFileReader(file) # reading the pdf
    print(reader.numPages) #print total number of pages in the pdf
    print(reader.getPage(0))  #print that perticular page
    
    page = reader.getPage(0)
    page.rotateCounterClockwise(180)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    
    with open('./pdfs/tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
import PyPDF2

with open('mypdf.pdf','rb') as pdf_file:
    pdf_obj = PyPDF2.PdfFileReader(pdf_file)

    print(pdf_obj.getPage(17).extract_text())
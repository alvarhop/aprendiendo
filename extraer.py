from traceback import print_tb
import PyPDF2


pdfFileObj = open("archivo.pdf",'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
textoPDF=""
for x in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(x)
    print(pageObj.extract_text())


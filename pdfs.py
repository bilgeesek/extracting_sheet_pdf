from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_writer = PdfFileWriter()
existing_pdf = open('Staj_başvuru.pdf', 'rb')
pdf_reader = PdfFileReader(existing_pdf)
num_pages = pdf_reader.numPages

for pagenum in range(num_pages - 18, num_pages - 17):
    obj = pdf_reader.getPage(pagenum)
    pdf_writer.addPage(obj)

output_file = open('Staj_başvuru2.pdf', 'wb')
pdf_writer.write(output_file)

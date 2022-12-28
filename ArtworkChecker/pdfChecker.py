import PyPDF2
from decimal import *
from paperCheck import *
# from printTest import printer

print('Please enter PDF File to Work With: ')
targetPDF = input()
pdfFile = targetPDF
readPDF = PyPDF2.PdfReader(pdfFile)

print('\n')
print(f'Here is some additional Info. about your File:')
#print(readPDF.metadata)

print("Author" +': ' + str(readPDF.metadata.author))
print("Creator" +': ' + str(readPDF.metadata.creator))
print("Creation Date" +': ' + str(readPDF.metadata.creation_date))
print("Subject" +': ' + str(readPDF.metadata.subject))
print("Producer" +': ' + str(readPDF.metadata.producer))
print("Title" +': ' + str(readPDF.metadata.title))

getPDF = readPDF.pages[0]
print(f'Total Pages within PDF document = {len(readPDF.pages)}')

# p = printer(readPDF)
s = sizeCheck(readPDF)
print(f'If your artwork is larger than standard paper sizes, please make sure the PDF height and width match the product you have ordered')


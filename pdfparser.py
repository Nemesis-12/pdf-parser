from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
import sys

usr = str(input("Enter Filename: "))
fp = open(usr, 'rb')
parser = PDFParser(fp)
password = " "
doc = PDFDocument(parser, password)
retstr = StringIO()
laparams = LAParams()

if not doc.is_extractable:
    print("An Unknown Error Has Occurred! \n Aborting...")
    sys.exit()

rsrcmgr = PDFResourceManager()
dev = TextConverter(rsrcmgr, retstr, laparams = laparams)
intrprt = PDFPageInterpreter(rsrcmgr, dev)

for page in PDFPage.create_pages(doc):
    intrprt.process_page(page)

text = retstr.getvalue()
fp.close()
dev.close()
retstr.close()
print(text)

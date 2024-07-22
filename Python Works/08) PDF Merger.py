from PyPDF2 import PdfWriter
import os
os.chdir("test PDFs")
merger = PdfWriter()
files = [pdf for pdf in os.listdir() if pdf.endswith(".pdf")]
x = len(files)
y = [files[i:i+1] for i in range(0,x)]
name = ''
for z in y:
  name = name + f"{z}"
name = name.replace("[", "").replace("]", "").replace(".pdf","-").replace('"','').replace('"','').replace("'",'')
name = name[:-1]
for pdf in files:
    merger.append(pdf)
merger.write(f"{name}_AllMerged.pdf")
merger.close()
print(os.getcwd())
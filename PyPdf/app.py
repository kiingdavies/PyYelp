# run: pipenv install pypdf2
# import PyPDF2 in app.py
# create an instance of PdfFileReader() instance on PyPDF2 
# Above the created PdfFileReader() instance , you need to run: with open("first.pdf", "rb") as file: then indent PdfFileReader() instance below
# first.pdf is the pdf file i downloaded into my project folder, rb meanings read in binary
# pass in *file* as the param in PdfFileReader() method. Save it as reader var
# print reader.numPages
# You can also run: reader.getPage(0) save in page var
# use the .rotateClockwise() method on page & pass in 90 as the value in the method
# use .PdfFileWriter() method on PyPDF2 & save in writer var
# Then call: writer.addPage(page) (u can also use insertPage method takes in page & index as params to rearrange the pages)
# Then call: with open("rotated.pdf" *name of the new pdf file to be created*, "wb" *write in binary*) as output:
# finally in the output block run: writer.write(output)
# run the program

import PyPDF2

with open("first.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("rotated.pdf", "wb") as output:
        writer.write(output)

# To combine multiple pdfs to one from scratch use the code below:
# import PyPDF2 
# call: .PdfFileMerger() on PyPDF2 & save it in merger var
# assume we have an array of files ["first.pdf", "second.pdf"] saved in file_names var
# then iterate over file_names array with for/in loop
# call the .append() method on merger & pass in file_name as param
# indent out of the code block and run: merger.write("combined.pdf") [combined.pdf is the name of the new Pdf file that would be create]
#run the program

import PyPDF2

merger = PyPDF2.PdfFileMerger()
file_names = ["first.pdf", "second.pdf"]
for file_name in file_names:
    merger.append(file_name)

merger.write("combined.pdf")


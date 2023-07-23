from docx import Document

numbersdone = 0
numberoffixes = 0
doc = Document('demo.docx')
for para in doc.paragraphs:
    newtext = ''
    for char in para.text:
        if char.isnumeric():
            numberoffixes += 1
            if numbersdone == 0:
                newtext += char
                numbersdone += 1
            else:
                newtext = newtext[:-1*numbersdone] + char + newtext[-1*numbersdone:]
                numbersdone += 1

        else:
            newtext += char 
            numbersdone = 0


    para.text = newtext

print(f'total fixes: {numberoffixes}')
doc.save('location to save the file')
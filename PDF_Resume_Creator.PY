from enum import auto
import json
from fpdf import FPDF

f = open("PDF_Resume_Creator.json", "r")
data = f.read()
info = json.loads(data)

pdf = FPDF("P", "mm", "Letter")
pdf.add_page()


for input in info:
    pdf.set_font("Courier", "", size = 15) 
    pdf.cell(200, 8, str(''), ln = 1, align = 'L')

    pdf.set_text_color(101, 109, 74)
    pdf.set_font("Times", "B", size = 30)
    pdf.cell(200, 15, str(input["titleP"]), border = True, ln = 1, align = 'C')

    pdf.set_text_color(127, 79, 36)
    pdf.set_font("Helvetica", "BI", size = 23)
    pdf.cell(200, 15, str(input["subtitleName"]), ln = 1, align = 'L')

    pdf.set_text_color(22, 26, 29)
    pdf.set_font("Courier", "", size = 15)
    pdf.cell(200, 6, str(input["occupation"]), ln = 1, align = 'L')
    pdf.cell(200, 6, str(input["address"]), ln = 1, align = 'L')
    pdf.cell(200, 6, str(input["number"]), ln = 1, align = 'L')
    pdf.cell(200, 6, str(input["email"]), ln = 1, align = 'L')
    pdf.cell(200, 6, str(input["githubAcc"]), ln = 1, align = 'L')
    pdf.cell(200, 8, str(''), ln = 1, align = 'L')

    pdf.set_text_color(101, 109, 74)
    pdf.set_font("Times", "B", size = 30)
    pdf.cell(200, 15, str(input["titleB"]), border = True, ln = 1, align = 'C')

    pdf.set_text_color(127, 79, 36)
    pdf.set_font("Arial", "BU", size = 20)
    pdf.cell(200, 15, str(input["subtitleEx"]), ln = 1, align = 'L')

    pdf.set_text_color(22, 26, 29)
    pdf.set_font("Courier", "", size = 15)
    pdf.cell(200, 6, str(input["company"]), ln = 1, align = 'L')
    pdf.cell(200, 6, str(input["position"]), ln = 1, align = 'L')
    pdf.cell(200, 6, str(input["yearEx"]), ln = 1, align = 'L')
    pdf.cell(200, 5, str(''), ln = 1, align = 'L')
    
    pdf.set_text_color(127, 79, 36)
    pdf.set_font("Arial", "BU", size = 20)
    pdf.cell(200, 15, str(input["subtitleEduc"]), ln = 1, align = 'L')

    pdf.set_text_color(22, 26, 29)
    pdf.set_font("Courier", "", size = 15)
    pdf.cell(200, 6, str(input["course"]), ln = 1, align = 'L')
    pdf.cell(200, 6, str(input["yearEduc"]), ln = 1, align = 'L')
    pdf.cell(200, 5, str(''), ln = 1, align = 'L')

    pdf.set_text_color(127, 79, 36)
    pdf.set_font("Arial", "BU", size = 20)
    pdf.cell(200, 15, str(input["subtitleSki"]), ln = 1, align = 'L')

    pdf.set_text_color(22, 26, 29)
    pdf.set_font("Courier", "", size = 15)
    pdf.cell(200, 6, str(input["sk1"]), ln = 1, align = 'L')
    pdf.cell(200, 6, str(input["sk2"]), ln = 1, align = 'L')
    pdf.cell(200, 6, str(input["sk3"]), ln = 1, align = 'L')
    pdf.cell(200, 6, str(input["sk4"]), ln = 1, align = 'L')
    pdf.cell(200, 6, str(input["sk5"]), ln = 1, align = 'L')
    pdf.cell(200, 5, str(''), ln = 1, align = 'L')

    pdf.set_text_color(127, 79, 36)
    pdf.set_font("Arial", "BU", size = 20)
    pdf.cell(200, 15, str(input["subtitleCour"]), ln = 1, align = 'L')

    pdf.set_text_color(22, 26, 29)
    pdf.set_font("Courier", "", size = 15)
    pdf.cell(200, 6, str(input["cor1"]), ln = 1, align = 'L')
    pdf.cell(200, 6, str(input["cor2"]), ln = 1, align = 'L')
    pdf.cell(200, 6, str(input["cor3"]), ln = 1, align = 'L')

pdf.output("Cabate_Resume.pdf")
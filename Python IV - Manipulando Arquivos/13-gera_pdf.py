from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World') #definindo altura, largura e texto
pdf.output('dados/exemplo.pdf') #o arquivo ira ser criado.
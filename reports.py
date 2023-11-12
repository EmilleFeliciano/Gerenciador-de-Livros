from modulos import *


class Relatorios():
    def printLivros(self):
        webbrowser.open("livro.pdf")
    def geraRelatLivros(self):
        self.c = canvas.Canvas("livro.pdf")

        self.codigoRel = self.codigo_entry.get()
        self.tituloRel = self.titulo_entry.get()
        self.descricaoRel = self.descricao_entry.get()
        self.autorRel = self.autor_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do livro')

        self.c.setFont('Helvetica-Bold', 15)
        self.c.drawString(50, 700, "Código:")
        self.c.drawString(50, 670, "Título:" )
        self.c.drawString(50, 640, "Descrição:" )
        self.c.drawString(50, 610, "Autor:" )

        self.c.setFont('Helvetica', 15)
        self.c.drawString(150, 700,  self.codigoRel)
        self.c.drawString(150, 670,  self.tituloRel)
        self.c.drawString(150, 640,  self.descricaoRel)
        self.c.drawString(150, 610,  self.autorRel)

        self.c.rect(20, 730, 550, 1, fill=False, stroke=True)

        self.c.showPage()
        self.c.save()
        self.printLivros()
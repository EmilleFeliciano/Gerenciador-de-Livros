from tkinter import *
from tkinter import ttk
import sqlite3


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

janela = Tk()

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

        self.c.setFont('Helvetica-Bold', 14)
        self.c.drawString(50, 700, "Código:")
        self.c.drawString(50, 670, "Título:" )
        self.c.drawString(50, 640, "Descrição:" )
        self.c.drawString(50, 610, "Autor:" )

        self.c.setFont('Helvetica', 12)
        self.c.drawString(150, 700,  self.codigoRel)
        self.c.drawString(150, 670,  self.tituloRel)
        self.c.drawString(150, 640,  self.descricaoRel)
        self.c.drawString(150, 610,  self.autorRel)

        self.c.rect(20, 730, 550, 1, fill=False, stroke=True)

        self.c.showPage()
        self.c.save()
        self.printLivros()

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.titulo_entry.delete(0, END)
        self.descricao_entry.delete(0, END)
        self.autor_entry.delete(0, END)

    def conecta_bd(self):
        self.conn=sqlite3.connect("livros.bd")
        self.cursor = self.conn.cursor(); print("Conectando ao Banco de Dados")

    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao Banco de Dados")

    def montaTabelas(self):
        self.conecta_bd()

    ## Criar tabela

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros(
            cod INTEGER PRIMARY KEY, 
            nome_titulo CHAR(40) NOT NULL,
            descricao CHAR(500), 
            autor CHAR(40)
            );
        """)
        self.conn.commit();print("Banco de Dados criado")
        self.desconecta_bd()
    
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.titulo = self.titulo_entry.get()
        self.descricao = self.descricao_entry.get()
        self.autor = self.autor_entry.get()

    def add_livro(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO livros (nome_titulo, descricao, autor)
                            VALUES (?, ?, ?)""",(self.titulo, self.descricao, self.autor))
        
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def select_lista(self):
        self.listaLiv.delete(*self.listaLiv.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_titulo, descricao, autor FROM livros
        ORDER BY nome_titulo ASC; """)
        for i in lista:
            self.listaLiv.insert("", END, values=i)
            self.conecta_bd()
            self.desconecta_bd()

    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaLiv.selection()

        for n in self.listaLiv.selection():
            col1, col2, col3, col4 = self.listaLiv.item(n, 'values')
        self.codigo_entry.insert(END,col1)
        self.titulo_entry.insert(END, col2)
        self.descricao_entry.insert(END, col3)
        self.autor_entry.insert(END, col4)
        


    def deleta_livro(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM livros WHERE cod = ? """,(self.codigo))
        self.conn.commit()
        self.desconecta_bd()

        self.limpa_tela()
        self.select_lista()

    def alterar_livro(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE livros SET nome_titulo = ?, descricao = ?, autor = ?
            WHERE cod = ? """,(self.titulo, self.descricao, self.autor, self.codigo))
        self.conn.commit()

        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def busca_livro(self):
        self.conecta_bd()
        self.listaLiv.delete(*self.listaLiv.get_children())

        self.titulo_entry.insert(END, '%')
        titulo = self.titulo_entry.get()
        self.cursor.execute(""" SELECT cod, nome_titulo, descricao, autor
        FROM livros WHERE nome_titulo LIKE '%s' ORDER BY nome_titulo ASC """ % titulo)
        buscanomeLiv = self.cursor.fetchall()
        
        for i in buscanomeLiv:
            self.listaLiv.insert("", END, values =i)

            self.limpa_tela()

        self.desconecta_bd()




class Application(Funcs, Relatorios):
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.widgets_primeiroFrame()
        self.lista_segundoFrame()
        self.montaTabelas()
        self.select_lista()
        self.Menus()
        janela.mainloop()

    def tela(self):
        self.janela.title("Gerenciador de Livros")
        self.janela.configure(background="#FFE4E1")
        self.janela.geometry("700x500")
        self.janela.resizable(True, True)
        self.janela.maxsize(width=900, height=700)
        self.janela.minsize(width=500, height=400)

    def frames_da_tela(self):
        self.primeiroFrame = Frame(self.janela, bd=4, bg="#FFE4E1",
                            highlightbackground="#759fe6", highlightthickness=2)
        self.primeiroFrame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.segundoFrame = Frame(self.janela, bd=4, bg="#FFE4E1",
                            highlightbackground="#759fe6", highlightthickness=2)
        self.segundoFrame.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_primeiroFrame(self):

        # Botão limpar tela

        self.bt_limpar = Button(self.primeiroFrame, text="Limpar", bd=2, bg='#FFF0F5',
                                 fg='#000000', font=('Verdana', 9, 'bold'), command= self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        #Botão buscar livros

        self.bt_buscar = Button(self.primeiroFrame, text="Buscar",bd=2, bg='#FFF0F5',
                                 fg='#000000', font=('Verdana', 9, 'bold'), command=self.busca_livro)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        #Botão Adicionar novo livro

        self.bt_novo = Button(self.primeiroFrame, text="Novo",bd=2, bg='#FFF0F5',
                                 fg='#000000', font=('Verdana', 9, 'bold'), command=self.add_livro)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        #Botão Alterar livro

        self.bt_alterar = Button(self.primeiroFrame, text="Alterar",bd=2, bg='#FFF0F5',
                                 fg='#000000', font=('Verdana', 9, 'bold'), command=self.alterar_livro)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        #Botão Apagar livro

        self.bt_apagar = Button(self.primeiroFrame, text="Apagar",bd=2, bg='#FFF0F5',
                                 fg='#000000', font=('Verdana', 9, 'bold'), command=self.deleta_livro)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

       
        #Criação da label e entrada do codigo

        self.lb_codigo = Label(self.primeiroFrame, text="Código", bg="#FFE4E1", fg='#000000')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.primeiroFrame, bg="#F5F5F5", fg='#000000')
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

         #Criação da label e entrada do título

        self.lb_titulo = Label(self.primeiroFrame, text="Título", bg="#FFE4E1", fg='#000000')
        self.lb_titulo.place(relx=0.05, rely=0.35)

        self.titulo_entry = Entry(self.primeiroFrame, bg="#F5F5F5", fg='#000000')
        self.titulo_entry.place(relx=0.05, rely=0.45, relwidth=0.5)

        #Criação da label e entrada da descricao

        self.lb_descricao = Label(self.primeiroFrame, text="Descrição", bg="#FFE4E1",fg='#000000')
        self.lb_descricao.place(relx=0.05, rely=0.6)

        self.descricao_entry = Entry(self.primeiroFrame, bg="#F5F5F5", fg='#000000')
        self.descricao_entry.place(relx=0.05, rely=0.7, relwidth=0.4, relheight=0.2)

        #Criação da label e entrada do Autor

        self.lb_autor = Label(self.primeiroFrame, text="Autor", bg="#FFE4E1",fg='#000000')
        self.lb_autor.place(relx=0.5, rely=0.6)

        self.autor_entry = Entry(self.primeiroFrame, bg="#F5F5F5", fg='#000000')
        self.autor_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
    

    def lista_segundoFrame(self):

        self.listaLiv = ttk.Treeview(self.segundoFrame, height= 3, column=('col1', 'col2', 'col3', 'col4'))
        self.listaLiv.heading("#0", text="")
        self.listaLiv.heading("#1", text="Código")
        self.listaLiv.heading("#2", text="Título")
        self.listaLiv.heading("#3", text="Descrição")
        self.listaLiv.heading("#4", text="Autor")
    

        self.listaLiv.column("#0", width=1)
        self.listaLiv.column("#1", width= 50)
        self.listaLiv.column("#2", width=200)
        self.listaLiv.column("#3", width=125)
        self.listaLiv.column("#4", width=125)
       

        self.listaLiv.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.segundoFrame, orient='vertical')
        self.listaLiv.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

        self.listaLiv.bind("<Double-1>", self.OnDoubleClick)

    def Menus(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.janela.destroy()
    
        menubar.add_cascade(label ="Opções", menu = filemenu)
        menubar.add_cascade(label = "Lista", menu = filemenu2)

        filemenu.add_command(label="Sair", command= Quit)
        filemenu.add_command(label="Limpar Livros", command= self.limpa_tela)

        filemenu2.add_command(label="Lista de Livros", command= self.geraRelatLivros)





Application()

from modulos import *
from validEntry import Validadores
from reports import Relatorios
from funcionalidades import Funcs
from screeninfo import get_monitors

janela = Tk()


def centralizar_janela(janela):
    
    monitor = get_monitors()[0]

    largura_janela = janela.winfo_reqwidth()
    altura_janela = janela.winfo_reqheight()

    # Calcule as coordenadas x e y para centralizar a janela
    x = monitor.width // 3 - largura_janela // 3
    y = monitor.height // 4 - altura_janela // 4

    # Defina a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")


centralizar_janela(janela)


class Application(Funcs, Relatorios, Validadores):
    def __init__(self):
        self.janela = janela
        self.validaEntradas()
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

        self.canvas_bt = Canvas(self.primeiroFrame, bd=0, bg='#FFF0F5', highlightbackground= '#D3D3D3',
                                highlightthickness=2)
        self.canvas_bt.place(relx=0.19,rely=0.08, relwidth=0.22, relheight=0.19)

        # Botão limpar tela

        self.bt_limpar = Button(self.primeiroFrame, text="Limpar", bd=2, bg='#FFF0F5',
                            activebackground='#FFB6C1', activeforeground='white',
                                 fg='#000000', font=('Verdana', 9, 'bold'), command= self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        #Botão buscar livros

        self.bt_buscar = Button(self.primeiroFrame, text="Buscar",bd=2, bg='#FFF0F5',
                                activebackground='#FFB6C1', activeforeground='white',
                                 fg='#000000', font=('Verdana', 9, 'bold'), command=self.busca_livro)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        #Botão Adicionar novo livro

        self.bt_novo = Button(self.primeiroFrame, text="Novo",bd=2, bg='#FFF0F5',
                              activebackground='#FFB6C1', activeforeground='white',
                                 fg='#000000', font=('Verdana', 9, 'bold'), command=self.add_livro)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        #Botão Alterar livro

        self.bt_alterar = Button(self.primeiroFrame, text="Alterar",bd=2, bg='#FFF0F5',
                                 activebackground='#FFB6C1', activeforeground='white',
                                 fg='#000000', font=('Verdana', 9, 'bold'), command=self.alterar_livro)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        #Botão Apagar livro

        self.bt_apagar = Button(self.primeiroFrame, text="Apagar",bd=2, bg='#FFF0F5',
                                activebackground='#FFB6C1', activeforeground='white',
                                 fg='#000000', font=('Verdana', 9, 'bold'), command=self.deleta_livro)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

       
        #Criação da label e entrada do codigo

        self.lb_codigo = Label(self.primeiroFrame, text="Código", bg="#FFE4E1", fg='#000000')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.primeiroFrame, bg="#F5F5F5", fg='#000000', validate = "key", validatecommand = self.vcmd4)
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

    def validaEntradas(self):
        self.vcmd4 = (self.janela.register(self.validate_entry4), "%P")

Application()

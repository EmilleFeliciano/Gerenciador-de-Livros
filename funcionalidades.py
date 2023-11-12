from modulos import *

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

        if self.titulo_entry.get() == "":
            msg= "Para cadastrar um novo livro é necessário \n"
            msg+= "um título."
            messagebox.showinfo("Cadastro de livros - Aviso!!", msg)
        else:

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

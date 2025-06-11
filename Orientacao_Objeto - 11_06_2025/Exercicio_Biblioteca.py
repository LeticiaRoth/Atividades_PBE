class ItemBiblioteca:
    #PARTE 1
    def __init__(self, titulo: str, ano_publicado: int, disponivel:bool):
        self.titulo = titulo
        self.ano_publicado = ano_publicado
        self.disponivel = disponivel

        #Metodo Emprestar
        #Uso o bool para declarar se ele estará disponível ou não
    def emprestar(self):
        if not self.disponivel:
            raise Exception(f"Livro {self.titulo}já está emprestado")
        self.disponivel = False

        # Metodo Devolver
    def devolver(self):
        if self.disponivel:
            raise Exception(f"Livro {self.titulo} está disponível")
        self.disponivel = True

        #Metodo Obter Info
    def obter_info(self):
        #Crio uma variável, para declarar se 'Sim' está disponível e 'Não' emprestado
        disponibilidade = "Sim" if self.disponivel else "Não"
        return f"Título: {self.titulo}, Ano: {self.ano_publicado} e Disponivel: {disponibilidade}"


    #PARTE 2
    #Coleção Livros herda de Item biblioteca
class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicado, disponibilidade):
        #Uso o Super para puxar da mãe
        super().__init__(titulo, ano_publicado, disponibilidade)
        self_livros = []


    def adicionar_livro(self,livro:ItemBiblioteca):
        self.livros.append(livro)

    def verificar_disponibilidade(self,disponibilidade):
        for livro in self_livros:
            if not livro.disponibilidade:
                return False
        return True

    def obter_info(self):
        retorno = super().obter_info()
        for livro in self.livros:
            #Chamo a função
            retorno += f'\n{livro.obter_info()}'
        return retorno



#Crio os objetos
livro1 = ItemBiblioteca("Dom Quixote", 1605, True)
livro2 = ItemBiblioteca("Senhora", 1808, False)


colecao = ColecaoLivros("Minha coleção", 2000, False)
print(colecao.obter_info())
print(colecao.verificar_disponibilidade(]))


#Printo os objetos criados, com a DEF obter info
print(livro1.obter_info())
print(livro2.obter_info())
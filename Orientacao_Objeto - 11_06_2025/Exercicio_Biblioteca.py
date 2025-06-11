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
        super().__init__(titulo, ano_publicado, disponibilidade)
        self.livros = []  # Corrigido: self.livros, não self_livros

    def adicionar_livro(self, livro: ItemBiblioteca):
        self.livros.append(livro)

    def verificar_disponibilidade(self):
        for livro in self.livros:
            if not livro.disponivel:  
                return False
        return True

    def obter_info(self):
        retorno = super().obter_info()
        for livro in self.livros:
            retorno += f'\n{livro.obter_info()}'
        return retorno


# Criação dos objetos
livro1 = ItemBiblioteca("Dom Quixote", 1605, True)
livro2 = ItemBiblioteca("Senhora", 1808, False)

colecao = ColecaoLivros("Minha coleção", 2000, False)
colecao.adicionar_livro(livro1)
colecao.adicionar_livro(livro2)

# Exibição
print(colecao.obter_info())
print(colecao.verificar_disponibilidade())

print(livro1.obter_info())
print(livro2.obter_info())
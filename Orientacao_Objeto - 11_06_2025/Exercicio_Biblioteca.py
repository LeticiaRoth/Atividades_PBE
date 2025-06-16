class ItemBiblioteca:
    #PARTE 1
    def __init__(self, titulo: str, ano_publicado: int, disponibilidade:bool):
        self.titulo = titulo
        self.ano_publicado = ano_publicado
        self.disponibilidade = disponibilidade

        #Metodo Emprestar
        #Uso o bool para declarar se ele estará disponível ou não
    def emprestar(self):
        if not self.disponibilidade:
            raise Exception(f"Livro {self.titulo}já está emprestado")
        self.disponibilidade = False

        # Metodo Devolver
    def devolver(self):
        if self.disponibilidade:
            raise Exception(f"Livro {self.titulo} está disponível")
        self.disponibilidade = True

        #Metodo Obter Info
    def obter_info(self):
        #Crio uma variável, para declarar se 'Sim' está disponível e 'Não' emprestado
        disponibilidade = "Sim" if self.disponibilidade else "Não"
        return f"Título: {self.titulo}, Ano: {self.ano_publicado} e Disponivel: {disponibilidade}"




    #PARTE 2
    #Coleção Livros herda de Item biblioteca (Herança)
class ColecaoLivros(ItemBiblioteca):
    #Atributos daquilo que será herdado
    def __init__(self, titulo, ano_publicado, disponibilidade):
        #Chama a classe pai, para que os atributos sejam devidamente inicializados
        super().__init__(titulo, ano_publicado, disponibilidade)

        #Cria um novo atributo chamado livros, uma lista que armazenará outros objetos do tipo ItemBiblioteca
        self.livros = []


    #Metodo que adiciona um objeto livro, que é uma instancia da classe ItemBiblioteca
    def adicionar_livro(self, livro: ItemBiblioteca):
        self.livros.append(livro)

    #Percorre a lista self.livros com for para verificar a disponibilidade;
    #Caso algum livro NAO ESTIVER DISPONIVEL, retorna False, se estiver Retorna True
    def verificar_disponibilidade(self):
        for livro in self.livros:
            #Se nao - False
            if not livro.disponivel:  
                return False
        #Se - True
        return True

    #Retorno = o metodo obter_info da superclasse ItemBiblioteca/ SOBRESCREVER
    def obter_info(self):
        retorno = super().obter_info()

        #Atribui o metodo a cda livro em self.livros
        for livro in self.livros:
            retorno += f'\n{livro.obter_info()}'
        return retorno





    #PARTE 3
class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicado, disponibilidade, edicao):
        #Puxo os atributos corretamente da classe Pai
        super().__init__(titulo, ano_publicado, disponibilidade)

        #Atributo edicao criado
        self.edicao = edicao


    #Agora edicao = nova_edicao, se passar pela excecao
    def atualizar_edicao(self, nova_edicao):
        if nova_edicao <= 0:
            raise ValueError("Número da edição menor que zero")
        self.edicao = nova_edicao


    #Revistas antes dos anos 2000, tem resticao de 7 dias
    def restringir_emprestimo(self,dias_max):
        if self.ano_publicado < 2000:
            return dias_max <= 7
        return True

    def obter_info(self):
        info_edicao = super().obter_info()
        #Sobrescrivi
        return f"{info_edicao} - Edição: {self.edicao}"





    #PARTE 4
class Biblioteca:
    def __init__(self):
        #Crio o dicionario para armazenar
        self.itens = {}


    #Adicionar titulos e barrar titulos duplicados
    def adicionar_item(self,item):
        if item.titulo in self.itens:
            raise ValueError("Título {item.titulo}já existe")
        #Adiciono uma chave ao dicionario com o valor item
        self.itens[item.titulo] = item


    #Remover titulos, s enoa for encontrado existe a excecao
    def remover_itens(self,titulo):
        if titulo not in self.itens:
            #Erro na chave, no caso nao encontrada
            raise KeyError(f"Título {titulo}, não encontrado")
        del self.itens[titulo]


    #Cria uma lista com os titulos disponiveis
    def listar_itens_disponiveis(self):
        return [titulo for titulo, item in self.itens.items() if item.disponibilidade]

    #Retorne o numero de itens emprestados
    def contar_itens_emprestados(self):
        return sum(1 for item in self.itens.values() if not item.disponibilidade)




    #PARTE 5
class RelatorioBiblioteca:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    #Verifica se há algum item na biblioteca
    def gerar_relatorio_completo(self):
        if not self.biblioteca.itens:
            return "Nenhum item na biblioteca."

        relatorio = "RELATÓRIO DA BIBLIOTECA DS18\n"
        #Busco nos valores do dicionario criado
        for item in self.biblioteca.itens.values():
            #Uso o metodo obter_info
            relatorio += f"- {item.obter_info()}\n"
        return relatorio.strip()


    #Retoorna um string com os titulos dos itens disponiveis e total
    def gerar_relatorio_disponibilidade(self):
        disponiveis = [
            titulo for titulo, item in self.biblioteca.itens.items()
            if item.disponibilidade
        ]

        relatorio = "ITENS DISPONÍVEIS:\n"
        if disponiveis:
            relatorio += "\n".join(f"- {titulo}" for titulo in disponiveis)
        else:
            relatorio += "Nenhum item disponível."


        #Retorna o total, pega o tamanho da lista
        relatorio += f"\n\nTotal disponíveis: {len(disponiveis)}"
        return relatorio



    #Retorna uma string com o nuero de itens emprestados e proporcao
    def gerar_relatorio_emprestimos(self):
        total = len(self.biblioteca.itens)
        emprestados = self.biblioteca.contar_itens_emprestados()

        if total == 0:
            proporcao = 0.0
        else:
            proporcao = emprestados / total

        relatorio = (
            "RELATÓRIO DE EMPRÉSTIMOS:\n"
            f"Total emprestados: {emprestados}\n"
            f"Proporção de emprestados: {proporcao:.2%}"  # Ex: 33.33%
        )
        return relatorio

"""
Instancia, objeto real criado com base no molde, os molde sã as classes
basicamente um objeto criado a partir de  uma classe


"""
# Criar algumas instancia
livro1 = ItemBiblioteca("Dom Casmurro", 1899, True)
livro2 = ItemBiblioteca("1984", 1949, True)
revista1 = Revista("Veja", 1998, True, 123)
colecao = ColecaoLivros("Coleção Tolkien", 2000, True)


# Adicionar livros à coleção
colecao.adicionar_livro(ItemBiblioteca("O Hobbit", 1937, True))
colecao.adicionar_livro(ItemBiblioteca("Senhor dos Anéis", 1954, True))


# Necessario criar a bibliotaca
biblioteca = Biblioteca()


# Adicionar itens na biblioteca, as intancias criadas
biblioteca.adicionar_item(livro1)
biblioteca.adicionar_item(livro2)
biblioteca.adicionar_item(revista1)
biblioteca.adicionar_item(colecao)


# Emprestar um livro
livro2.emprestar()  # 1984 fica indisponível
revista1.emprestar()  # Veja fica indisponível


# Criar relatório
relatorio = RelatorioBiblioteca(biblioteca)

# Imprimir relatórios
print(relatorio.gerar_relatorio_completo())
print()
print(relatorio.gerar_relatorio_disponibilidade())
print()
print(relatorio.gerar_relatorio_emprestimos())


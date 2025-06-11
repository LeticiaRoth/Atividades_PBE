"""

1. Criar a classe Produto com os atributos
- nome
- preço -> privado

2. Implemente um metodo para exibir_dados(), que imprime o nom e o preço

3. Crie os getter e setter do preço

4. Criar a classe Carrinho com:
    -atributo itens (lista incialmente vazia)

5. Métodos da classe Carrinho:
- adicionar(produto) - recebe um Produto e adiciona a lista de itens

-remover(produto) - remove o produto da lista itens

- total() - RETORNA a soma dos preços dos preços dos produtos no carrinho

-listar_itens() - Imprime todos os produtos com seu preço
"""

#Parte 1
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    #Parte 2
    def exibir_dados(self):
        print(f"Nome produto: {self.nome} e Pre  ço produto: {self.__preco}")

    #Parte 3 - GETTER e SETTER
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self,preco):
        if preco < 0:
            raise ValueError ("Inválido")
        self.__preco = preco

#Parte 4
class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto):
        self.itens.append(produto)

    def remover(self,produto):
        self.itens.remove(produto)

    def total(self):
        soma = 0
        for produto in self.itens:
            soma += produto.preco
        return soma

    def listar_itens(self):
        print("Itens no carrinho:")
        for produto in self.itens:
            produto.exibir_dados()
        print(f"Total: R${self.total():.2f}")

#Criação dos produtos
produto1 = Produto("Sabão", 12)
produto2 = Produto("Limão", 4)
produto3 = Produto("Coca-Cola", 9)

#Adiciono ao objeto carrinho com a Classe Carrinho
carrinho = Carrinho()
carrinho.adicionar(produto1)
carrinho.adicionar(produto2)
carrinho.adicionar(produto3)

carrinho.listar_itens()
"""ENCAPSULAMENTO - o que pode e não pode ser acessado na classe"""


class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular

        # .__ = encapsula o parametro e atributo saldo
        self.__saldo = saldo

    """
    # Para pegar o valor encapsulado
    def get_saldo(self):
        return self.__saldo

    # Ele altera o valor encapsulado
    def set_saldo(self, valor):
        if valor < 0:
            # Trata o erro
            raise ValueError("Saldo não pode ser negativo")
        self.__saldo = valor
    """

    #@ é uma atribuição a mais, um decorator, atribuições padrões para algo a mais dentro da função
    #Algo a mais que a função padrão não faz, adiciona sme alterar o padrão

    #Funciona como um GET
    @property
    def saldo(self):
        return self.__saldo

    #Funciona como um SET, ele precisa do property para funcionar
    @saldo.setter
    8


    #Simula a função de sacar, como uma conta bancária
    def sacar(self,valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            raise ValueError("Valor maior que o saldo disponível")


conta_bancaria123 = ContaBancaria("Israel", 1000)
print(conta_bancaria123.titular)

conta_bancaria123.__saldo =12222
print(conta_bancaria123.saldo)

conta_bancaria123.saldo =1100
print(conta_bancaria123.saldo)


"""
# Printo o valor antigo, ele mostra o valor encapsulado
print(conta_bancaria123.get_saldo())

# Altera o valor dentor do encapsulamento de 1000 para 20
conta_bancaria123.set_saldo(20)

#Usa a função sacar e agora o valor é 15
conta_bancaria123.sacar(5)

#Utilização da propriedade de modo seguro
print(conta_bancaria123.__saldo)
"""

#Trabalhará com a classe abstrata
from abc import ABC, abstractmethod

class Pagamento(ABC):

    @abstractmethod
    def estorno(self, valor):
        #Passa adianta, continue
        pass

    @abstractmethod
    def autorizar(self, valor):
        pass


#Herda da classe Pagamento
class PIX(Pagamento):
    def __init__(self, chave):
        self.chave = chave

    def estorno(self, valor):
        print(f"Estornando {valor} via PIX")

    def autorizar(self, valor):
        print(f"Pagamento no valor de {valor} autorizado via PIX")


pix123 = PIX("senai123")
pix123.autorizar(1500)
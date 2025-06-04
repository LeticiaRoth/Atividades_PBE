#Classe começa com maisculo
class Pessoa:
    def __init__(self, nome, idade, cpf,rg):
        self.nome = nome
        self.idade = idade
        self.cpf =cpf
        self.rg =rg
        #Não estou atribuindo parâmetor e sim um atributo
        self.escolaridade = "Superior Completo"

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

    #Tranformar em STRING o que será printado
    def __str__(self):
        return f'{self.nome} - {self.idade}'

    #Igualdade, para ver se são iguais
    def __eq__(self, other):

        #pessoa1 == other, pode ser o que quiser
        if  isinstance(other, Pessoa):

            #Para verificar se realmente é uma pessoa, preciso verificar todos os atributos
            if self.nome == other.nome and self.idade == other.idade and self.cpf == other.cpf and self.rg == other.cpf:
                return True
            return False

    #Utilizando para ver o tamanho, listas e até strings
    def __len__(self):
        return  self.idade


#Criei uma classe e depois um objeto com seus atributos
pessoa1 = Pessoa("André", 22, 123456789,"3456677678")

#Puxei a apresentação com a função
pessoa1.apresentar()

#Usei o print, para isso preciso utilizar a def__str__
print(pessoa1)


"""
Anotações de MAIOR, MAIOR IGUAL, MENOR, MENOR IGUAL

< - def__lt__(self,other

<= - def__le__(self,other)

> - def__gt__(self,other)

>= - def__ge__(self,other)
"""


"""HERANÇA"""
#Herda os atributos da classe Pessoa, com nome, idade, cpf,rg e apresentação
# () - significa quem é a mãe dele
class Funcionario(Pessoa):

    #Atrinuo mais um - cargo
    def __init__(self, nome, idade, cpf,rg, cargo):
        #Pegar da classe mãe ou pai
        super().__init__(nome,idade,cpf,rg)
        self.cargo = cargo

    def trabalhar(selfs):
        print("trabalhando")

    """POLIMORFIMOS - mesma função, funcionalidade diferentes"""
    #No caso puxo a apresentação da classe Pessoa, mesma função com finalidade diferente
    def apresentar(self):
        print(f"Olá meu nome é {self.nome} e trabalho como {self.cargo}")


#Dentro do pai ou mãe já tinha a função apresentar
funcionario = Funcionario("Giovana", 19,"23344555", "676777777", "Instrutora")

#Coloco o objeto e a chamofunção
funcionario.trabalhar()


#Coloco o objeto e a chamo a função
funcionario.apresentar()


#Verificar se é pessoa ou não, foi colocado dentro da função igualdade
#Se o objeto é igual a classe
print(isinstance(funcionario,Pessoa))

print(funcionario.nome)
funcionario.nome = "Enzo"
print(funcionario.nome)



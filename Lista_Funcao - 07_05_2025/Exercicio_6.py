def classificacao_cinema():
    for idade in lista_idade:
        if idade < 18:
            print("Filme proibido para -18 anos")
        else:
            print("Filme liberado (+18)")
        
lista_idade = [15, 20, 8]
classificacao_cinema()
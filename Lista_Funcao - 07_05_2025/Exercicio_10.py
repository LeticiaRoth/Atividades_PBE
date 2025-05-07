def jogo_classificacao():
    for numero in numeros:
        if numero < 5:
            print("Pequeno")
        elif numero >= 6 and numero <= 9:
            print("Médio")
        else:
            print("Grande")
    
numeros = [3, 9, 12]
jogo_classificacao()
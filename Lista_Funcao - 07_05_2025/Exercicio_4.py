def jogo_tabuleiro(numeros):
    for numero in numeros:
        if numero % 2 == 0:
            print(f"Número par {numero} - AVANÇAR")
        else:
            print(f"Número ímpar {numero}- RECUAR")


numeros = [4, 7, 10]
(jogo_tabuleiro(numeros))
def palindromos(titulos):
    for palavra in titulos:
        palavras = ''.join(c.lower() for c in palavra if c.isalnum())
        if palavras == palavras[::-1]:
            print(f"{palavra} é um palindromo")
        else:
            print(f"{palavra} não é um palíndromo")

titulos = ["Ana ana", "1DSTB-SENAI", "Subi no onibus"]
palindromos(titulos)
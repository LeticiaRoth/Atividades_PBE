def calculo_letras(palavras):
    quantidade_letras = [len(palavra) for palavra in palavras]
    
    for palavra, quantidade in zip(palavras, quantidade_letras):
        print(f"A palavra {palavra} tem {quantidade} letras")

palavras = ["Casa", "Paralelepípedo", "Python"]
calculo_letras(palavras)

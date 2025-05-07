def tabuada():
    for numero in numeros_tabuada:
        print(f"\nTabuada do {numero}:")
        
        for multiplicacao in range(1, 11):
            resultado = numero * multiplicacao
            print(f"{numero} X {multiplicacao} = {resultado}")

numeros_tabuada = [2, 3, 4]
tabuada()

def fatorial():
    numeros = [3, 7,9,25,26]
    for numero in numeros:
        fatorial = 1 
        for i in range(1, numero+1):
            fatorial *= i
        print(f"Fatorial de {numero} é {fatorial}")
        
fatorial()
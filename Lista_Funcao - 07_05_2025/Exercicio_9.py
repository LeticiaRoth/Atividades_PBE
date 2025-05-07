def conversao_fahrenheit():
    lista_fahrenheit = []
    for temperatura in temp_celsius:
        temp_fahrenheit = (temperatura * 9/5) + 32
        lista_fahrenheit.append(temp_fahrenheit)
    return lista_fahrenheit

temp_celsius = [30, 100, 0]
print(conversao_fahrenheit())

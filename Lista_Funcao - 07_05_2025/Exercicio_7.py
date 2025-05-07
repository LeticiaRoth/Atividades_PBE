def calculo_desconto():
    desconto = []
    for preco in produtos:
        preco_desconto = preco * 0.9
        desconto.append(preco_desconto)
    return desconto
    
produtos = [50, 120, 200]
print(calculo_desconto())
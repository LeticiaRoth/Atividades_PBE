def dobro_promocao():
    promocao1 = produto1 * 2
    promocao2 = produto2 * 2
    promocao3 = produto3 * 2
    return promocao1, promocao2, promocao3

produto1 = 5
produto2 = 8
produto3 = 12


promocao1, promocao2, promocao3 = dobro_promocao()

print(f"Produto A R${produto1} agora custa R${promocao1}")
print(f"Produto B R${produto2} agora custa R${promocao2}")
print(f"Produto C R${produto3} agora custa R${promocao3}")

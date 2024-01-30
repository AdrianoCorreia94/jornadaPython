'''
    Aninhar listas
'''

frutas = ['Laranja', 'Pera', 'Uva']
valor = [3.99, 4.50, 12]
ud = ['kg', 'kg', 'kg']
tabela_preco = [frutas, valor, ud]

print(tabela_preco)

print(tabela_preco[0])  # retorna a lista no posicao indicada

# retornar o item indicado da lista da posicao indicada
print(tabela_preco[0][1])
print(tabela_preco[1][1])
print(tabela_preco[2][1])
print('-'*20)


# iterar cada lista dentro da lista
for lista in tabela_preco:
    print(lista)
    print('-'*20)

# iterar o item de cada lista dentro da lista
for lista in tabela_preco:
    for item in lista:
        print(item)
print('-'*20)

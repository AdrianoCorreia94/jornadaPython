'''
    Acessando dados de uma lista atraves de fatiamento
'''


# %%
# criacao da primeira lista
frutas = ['Manga', 'Uva', 'Abacate', 'Banana', 'Caqui']

# criacao da segunda lista para adicionar a primeira
frutas2 = ['Morango', 'Abacaxi', 'Acai', 'Laranja', 'Limao']


# adicionar lista secundaria à primeira
frutas.extend(frutas2)


# FATIAMENTO
# fatiar a lista
print(frutas[3:7])

# fatiar do inicio ao fim (seria o mesmo que imprimir inteira)
print(frutas[:])

# fatiamento do ultimo para o primeiro
print(frutas[-1:0:-1])

# fatiamento de alguma posicao ate a ultima
print(frutas[4::])

# fatiamento de ultima ate alguma indicada
# fatia do ultimo item ate o item no indice indicado (nao incluindo o indicado)
print(frutas[-1:2:-1])

# fatiar os 3 ultimos
print(frutas[-1:-4:-1])

'''
    iterando dados de uma lista
'''


# %%
# criacao da primeira lista
frutas = ['Manga', 'Uva', 'Abacate', 'Banana', 'Caqui']

# criacao da segunda lista para adicionar a primeira
frutas2 = ['Morango', 'Abacaxi', 'Acai', 'Laranja', 'Limao']


# adicionar lista secundaria à primeira
frutas.extend(frutas2)


# ITERANDO
# iterar item a item
for item in frutas:
    print(item)

# iterando com indice de posicao dos itens
for indice, item in enumerate(frutas):
    print(indice, item)

# iterando por ordem reversa da lista
for item in reversed(frutas):
    print(item)


# iterando por ordem reversa da lista com indice
for indice, item in enumerate(reversed(frutas)):
    print(indice, item)


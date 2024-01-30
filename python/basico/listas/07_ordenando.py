'''
    Ordenar uma lista
'''

# %%
# criacao da primeira lista
frutas = ['Manga', 'Uva', 'Abacate', 'Banana', 'Caqui']

# criacao da segunda lista para adicionar a primeira
frutas2 = ['Morango', 'Abacaxi', 'Acai', 'Laranja', 'Limao']


# adicionar lista secundaria à primeira
frutas.extend(frutas2)

print(frutas)


ordem_crescente = frutas.copy()  # copia para ordenar de forma crescente
ordem_decrescente = frutas.copy()  # copia para ordenar de foorma decrescente

# ordem alfabetica crescente
ordem_crescente.sort()
print(ordem_crescente)

# ordem alfabetica decrescente
ordem_decrescente.sort(reverse=True)
print(ordem_decrescente)

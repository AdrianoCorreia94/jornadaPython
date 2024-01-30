'''
    Adicionar lista a uma outra lista
'''

# %%
# criacao da primeira lista
frutas = ['Manga', 'Uva', 'Abacate', 'Banana', 'Caqui']

# criacao da segunda lista para adicionar a primeira
frutas2 = ['Morango', 'Abacaxi', 'Acai', 'Laranja', 'Limao']


# adicionar lista secundaria à primeira
frutas.extend(frutas2)
print(frutas)
# %%

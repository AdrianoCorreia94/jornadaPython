'''
    Acessando dados de uma lista
'''


# %%
# criacao da primeira lista
frutas = ['Manga', 'Uva', 'Abacate', 'Banana', 'Caqui']

# criacao da segunda lista para adicionar a primeira
frutas2 = ['Morango', 'Abacaxi', 'Acai', 'Laranja', 'Limao']


# adicionar lista secundaria à primeira
frutas.extend(frutas2)
print(frutas)


# ACESSANDO
# %%
# acesso direto por index
print(frutas[0]) # acessa o item na posicao do arg

# acesso indice de um elemento
print(frutas.index('Morango')) 



# %%

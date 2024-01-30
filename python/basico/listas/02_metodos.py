'''
    Principais metodos das litas
'''
# %%

# criacao da lista
frutas = ['Manga', 'Uva', 'Abacate', 'Banana', 'Caqui']

# METODOS

# ver tamanho da lista
print(len(frutas))
print(f"A lista possui {len(frutas)} elementos")


# metodos de adicao
frutas.append('Melao')  # adiciona ao final da lista
frutas.append('Abacaxi')

# %%
frutas.insert(0, 'Pitanga')  # adiciona ao index indicado no argumento
frutas.insert(1, 'Morango')
frutas

# %%
# metodos de exclusao
copia = frutas.copy()  # metodo para criar copia da lista

# %%
print('Lista completa')
print(copia)

print('Remover o Caqui com metodo remove')
copia.remove('Caqui')  # remover por valor do item
print(copia)


print('Remover o item na posicao 1 com metodo pop')
copia.pop(1)  # remover item da posicao indicada
print(copia)


print('Remover o item na posicao 2 com metodo del')
del copia[2]  # remover por valor do argumento
print(copia)

# APAGAR LISTA COMPLETA
# %%
print('Limpar lista com metodo clear')
copia.clear()
print(copia)
# %%

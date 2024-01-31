'''
    Acessando itens de uma tupla
'''
# criacao
fruta = ('Laranja', 'Uva', 'Morango',)

print(f'\ntupla original \n{fruta}')
print(f'tamanho da tupla: {len(fruta)} registros\n')

# acesso por indice
print(f"posicao 0: {fruta[0]}")
print(f"posicao 1: {fruta[1]}")
print(f"posicao 2: {fruta[2]}")
print(f"ultima posicao: {fruta[-1]}\n")

# acesso por fatiamento
print('FATIAMENTO')
print(f"Fatiamento do primeiro à posicao 1: {fruta[0:2]}")
print(f"Fatiamento do ultimo à posicao 1: {fruta[-1:0:-1]}")
print(f"Fatiamento do ultimo à posicao 0: {fruta[-1::-1]}\n")


'''
    PRINCIPIOS DE PILHA
'''

# criacao da primeira lista
frutas = ['Manga', 'Uva', 'Abacate', 'Banana', 'Caqui']

# criacao da segunda lista para adicionar a primeira
frutas2 = ['Morango', 'Abacaxi', 'Acai', 'Laranja', 'Limao']


# adicionar lista secundaria à primeira
frutas.extend(frutas2)

print(f"\nLISTA INICIAL \n{frutas}\n")

# LAST IN FIRST OUT

print('ultimo a entrar primeiro a sair')
frutas.pop()
print(frutas)
frutas.pop()
print(frutas)
frutas.pop()
print(frutas)

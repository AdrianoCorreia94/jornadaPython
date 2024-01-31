'''
    Tuplas sao do tipo imutavel, "nao possui metodos como as listas"
    Aceitam diferentes tipos de objetos
'''

# sempre terminuar com virgular para evitar conflito no sistema
# cada cadeia de strings representa um elemento
fruta = ('Laranja', 'Uva', 'Morango',)
print(fruta)
for x in fruta:
    print(x)
print(f'{"-"*30}\n')


pais = tuple('Brasil')  # cada letra representa um elemento
print(pais)

for x in pais:
    print(x)
print(f'{"-"*30}\n')

nome = (['Ana', 'Bruno', 'Chris'], 19, )  # tupla de listas
print(nome)

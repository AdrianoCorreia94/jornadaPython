paises = (('Brasil', 'Argentina', 'Uruguai'),
          ('Estados Unidas', 'Mexico', 'Canada'),
          ('Espanha', 'Alemanha', 'Italia'),)

print(paises)
print()

# iterar cada tupla da tupla
print('ITERAR CADA TUPLA DENTRO DA TUPLA')
for tupla in paises:
    print(tupla)

# iterar cada item da tupla 
print('\nITERAR CADA ITEM')
for tupla in paises:
    for pais in tupla:
        print(pais)

print('\nITERAR INDICE E VALOR DE CADA TUPLA')
for indice, valor in enumerate(paises):
    print(indice, valor)

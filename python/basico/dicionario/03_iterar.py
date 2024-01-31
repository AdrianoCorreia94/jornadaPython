quadrados = {x: x**2 for x in (1, 2, 3, 4, 5, 6, 7, 8, 9)}
quadrados

# iterar sobre chaves e valores
for key, item in quadrados.items():
    print(key, item)

# acessar as chaves
for x in quadrados:
    print(x)

for y in quadrados.keys():
    print(y)

# iterando sobre os valores
for v in quadrados.values():
    print(v)

# enumerando as chaves
for e, k in enumerate(quadrados.keys()):
    print(e, k)

# enumerando os valores
for e, v in enumerate(quadrados.values()):
    print(e, v)

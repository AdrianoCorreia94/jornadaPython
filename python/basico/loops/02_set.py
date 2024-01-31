# eliminando duplicatas

inteiros = [1, 2, 3, 4, 1, 3, 4, 5, 6, 7, 7, 7]

for i in set(inteiros):
    print(i)

novo = set(inteiros)
print(f'nova lista de inteiros sem duplicatas {novo}')

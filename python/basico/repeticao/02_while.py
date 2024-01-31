# simples
x = 0

# enquanto x for menor que 3, mostarar e adicionar 1 ao x
while x < 3:  # x vai de 0 a 2
    print(x)
    x += 1

while x <= 3:
    print(x)  # x vai de 0 a 3
    x += 1


y = 0
# estrutura base para uma instrucao mais rebuscada utilizando bool
while True:
    if y < 3:
        print(f'Y vale {y}')
        y += 1
        continue
    else:
        break

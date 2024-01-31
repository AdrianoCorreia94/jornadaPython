# carregando dados na memoria

# abrindo na memoria e lendo os dados
# indicado para grande quantidade de dados (streaming)
with open('colors.txt', 'r') as arquivo:
    for line in arquivo:
        print(line)


# salvando em um objeto python
dados = open('colors.txt', 'r')

print(dados.read())


for line in dados:
    print(line)


# abrindo e salvando em outro objeto
with open('colors.txt', 'r') as arquivo:
    teste = arquivo.read()

print(f'teste = {teste}')

# abrindo arquivo e salvando na memoria
with open('teste.txt', 'a') as novo:
    for line in teste:
        novo.writelines(line)

# utilizando funcao zip

cifras = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
notas = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']

for cifra, nota in zip(cifras, notas):
    print(cifra, nota)
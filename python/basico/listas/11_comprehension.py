# criar uma lista com codigo simplificado

# criar uma lista com pares entre 1 e 15
pares = [x for x in range(15) if x % 2 == 0]
print(f"PARES: {pares}")

# criar uma lista com impares entre 1 e 15
impares = [x for x in range(16) if x % 2 != 0]
print(f"IMPARES: {impares}")

# permitir entrada se a pessoa for listada como convidado
convidados = ['Hanna', 'Carl', 'Will', 'Bob', 'Luigi']
comparecidos = ['Annie', 'Mario', 'Carl', 'Yan', 'Hanna']

permitidos = [x for x in comparecidos if x in convidados]
print(f'\nCONVIDADOS\nPERMITIR A ENTRADA DE {permitidos}')

# ver quem faltou ao evento
ausentes = [x for x in convidados if x not in comparecidos]
print(f'\nAUSENTES\nNAO COMPARECERAM AO EVENTO: {ausentes}\n')
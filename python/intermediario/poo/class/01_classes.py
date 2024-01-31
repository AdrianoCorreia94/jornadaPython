# criar classe pessoa
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade


# instanciar classe
mary = Pessoa('Mary', 24) # instancia da class Pessoa
eron = Pessoa('Eron', 31)  # instancia da class Pessoa

print(mary)  # retornara o objeto e seu local na memoria

print(mary.nome)  # retorna o atributo nome de mary
print(eron.idade)  # retorna o atributo idade de eron

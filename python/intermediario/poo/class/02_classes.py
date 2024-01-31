'''
    ALTERANDO O RETORNO DE OBJETO
'''

# criar classe pessoa


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:  # alterar o tipo de retorno do objeto
        return (f"{self.nome} tem {self.idade} anos de idade")


# instanciar classe
mary = Pessoa('Mary', 24)  # instancia da class Pessoa
eron = Pessoa('Eron', 31)  # instancia da class Pessoa

# antes retornava o objeto e seu local na memoria, agora retorna a func __str__
print(mary)

print(mary.nome)  # retorna o atributo nome de mary
print(eron.idade)  # retorna o atributo idade de eron

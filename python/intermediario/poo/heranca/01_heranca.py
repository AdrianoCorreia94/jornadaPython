class Animal:
    def __init__(self, especie):
        self.especie = especie


class Cachorro(Animal):  # classe cachorro herda de animal
    def __init__(self, especie, raca, cor):
        super().__init__(especie)  # herdando o atributo especie
        self.raca = raca  # incluindo atributo raca
        self.cor = cor  # incluindo atributo cor

    def __str__(self) -> str:
        return f'{self.especie} {self.raca} {self.cor}'


class Passaro(Cachorro):  # herda da classe cachorro e inclui atributo voa
    def __init__(self, especie, raca, cor, voa: bool):
        super().__init__(especie, raca, cor)
        self.voa = voa

    def __str__(self) -> str:
        return f'{super().__str__()} voa:{self.voa}'
# instanciando


dog = Cachorro('Domestico', 'Husky', 'cinza')
bird = Passaro('Pinguin', 'King', 'Branco e Preto', False)

print(dog)
print(bird)  # bird herdou o __str__ de dog

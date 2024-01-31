# CRIANDO DICIONARIOS

# com valores e chaves definidos
alunos = {'Matricula': 1, 'Aluno': 'Annie'}
feriados = dict(dezembro=25, janeiro=1, setembro=7, novembro=[2, 15])

print(alunos)
print(feriados)
# criando dicionarios vazio
produtos = dict()
metas = {}

# adicionando item ao dicionario vazio
produtos['Descricao'] = 'ProdutoA'
produtos['Categoria'] = 'CategoriaA'
print(produtos)

metas['dia'] = 'segunda-feira'
metas['meta'] = 'Meta 1'
print(metas)

# %%
# dicionarios com chaves
emergencias = ([('Samu', 192), ('Policia', 190), ('Bombeiros', 193)])
print(emergencias)

# %%
# criando com comprehension
quadrados = {x: x**2 for x in (1, 2, 3, 4, 5, 6, 7, 8, 9)}
quadrados
# %%

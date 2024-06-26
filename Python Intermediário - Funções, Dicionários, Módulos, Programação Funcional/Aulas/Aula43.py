import copy

from Ex43 import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novosProdutos = [
    {**p, 'preco': round(p['preco']*1.1, 2)}
    for p in copy.deepcopy(produtos)
]
print(*produtos, sep='\n')
print()
print(*novosProdutos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

ordemProdutos = sorted(
    novosProdutos,
    key=lambda p:p['nome'], reverse=True
)
print()
print(*novosProdutos, sep='\n')
print()
print(*ordemProdutos, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

precoProdutos = sorted(
    copy.deepcopy(novosProdutos),
    key=lambda p:p['preco']
)
print()
print(*novosProdutos, sep='\n')
print()
print(*precoProdutos, sep='\n')

# reforçar essa materia
# TODO
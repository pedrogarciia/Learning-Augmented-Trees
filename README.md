# Learning-Augmented Search Trees (Projeto Acadêmico)

Projeto desenvolvido para explorar, na prática, o conceito de **Learning-Augmented Data Structures**, com foco em árvores de busca.

A proposta é demonstrar como previsões (simulando Machine Learning) podem ser utilizadas para **melhorar o desempenho médio** de estruturas clássicas, adaptando a organização da árvore ao padrão de uso dos dados.

---

## Ideia Central

Estruturas tradicionais como **BST, AVL e Red-Black Trees** garantem eficiência no pior caso (**O(log n)**), mas não consideram padrões reais de acesso.

Este projeto simula uma abordagem *learning-augmented*, onde:

- Elementos mais acessados são posicionados **mais próximos da raiz**
- Elementos menos acessados ficam em níveis mais profundos

Resultado: buscas frequentes se tornam mais rápidas na prática.

---

## Como Funciona

O projeto utiliza:

- Uma **árvore binária de busca (BST)**
- Um sistema de **previsão de frequência de acesso** (simulado)

Essas previsões são usadas para:

1. Definir quais elementos devem ficar próximos da raiz
2. Construir a árvore priorizando esses elementos
3. Reduzir o custo médio das buscas

---

## Simulação de Machine Learning

O projeto não implementa um modelo real de ML.

Em vez disso, utiliza um dicionário como:

```python
predicted_frequencies = {
    20: 100,
    10: 60,
    30: 40,
    5: 10,
    15: 8
}

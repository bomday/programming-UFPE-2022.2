# Competição

**Limite de tempo do código: 1000ms**

Quantidade de diamantes é uma boa forma de medir riqueza no Minecraft pois é um dos recursos minerais mais difícil de ser encontrado e minerado no mapa.

Arthur, Luiz e Pedro decidiram fazer uma competição no Minecraft, para decidir quem iria escolher qual brega que irá tocar durantes suas longas noites de programação no CIn e pediram ajuda de Tantan para disponibilizar suas vilas como moradia para cada um. Foi combinado que a competição iria ser realizada dentro do jogo, na qual cada participante iria criar um mundo do zero e teria que encontrar o máximo de diamantes no tempo definido.

Para deixar a competição mais divertida, eles combinaram que cada um iria definir uma restrição para o programa que computaria qual o maior valor de diamantes encontrado pelos participantes.

- Luiz definiu que o programa não poderia utilizar nenhuma estrutura condicional em seu código, como IF e outras;
- Pedro proibiu a utilização de quaisquer funções de bibliotecas externas para calcular o máximo da quantidade de diamantes do vencedor;
- Arthur falou que, para encontrar o valor final da quantidade máxima de diamantes, seria obrigatório utilizar a seguinte função para encontrar o máximo entre 2 valores: x = (a + b + (|a - b|)) / 2.

Visando deixar a solução mais simples, Arthur e Pedro chegaram a um acordo e decidiram que seria permitido utilizar funções externas para calcular o valor absoluto de um número (abs(), em Python).

Sua tarefa é escrever o programa que vai auxiliar os três a descobrir o vencedor da competição, em acordo com todas as restrições.

## Input:

```
A
L
P
H
```
- A - número natural
- L - número natural
- P - número natural
- H - número natural (1 <= H)

As três primeiras linhas representam a quantidade média de diamantes obtidos por hora de Arthur, Luiz e Pedro, respectivamente.

A quarta linha de entrada é composta por um valor que representa a duração da competição, em horas.

**obs:** Você deve considerar que a entrada é amigável, ou seja, sempre estará dentro do formato descrito.

## Output:

```
M
```

- M - número natural

## Exemplos:

### Caso 1:

Input:
```
1
2
3
1
```

Output:
```
3
```

### Caso 2:

Input:
```
5
5
5
5
```

Output:
```
25
```

### Caso 3:

Input:
```
1
10
100
2
```

Output:
```
200
```
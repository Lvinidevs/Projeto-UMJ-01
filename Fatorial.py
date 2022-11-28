# Disciplina   : Algoritmos e Estrutura de dados
# Professor(a)   :  Nathalia Menezes
# Descrição   : Calcular o fatorial de um determinado número
# Autor(a)    : Lucas Vinicius da Silva
# Matricula   : 2022206348
# Data atual  :  21/10/2022


# Fatorial  
from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))

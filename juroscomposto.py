# Disciplina   : Algoritmos e Estrutura de dados
# Professor(a)   :  Nathalia Menezes
# Descrição   : juros composto
# Autor(a)    : Lucas Vinicius da Silva
# Matricula   : 2022206348
# Data atual  :  21/10/2022

#Calculadora de juros composto
C = float(input("Capital: "))
i = float(input("Taxa: "))
t = float(input("Tempo: "))

M = C*(1 + i)**t
print('Valor fututo: {}'.format(M))
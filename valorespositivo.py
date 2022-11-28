# Disciplina : Algoritmos e Estrutura de dados
# Professor(a) : Nathalia Menezes
# Descrição    :  Leitura de Valores inteiros positivo e calcula a média dos mesmos
# Alunor(a)    : Lucas Vinicius da Silva
# Matricula    :  2022206348
# Data atual   :  21/10/2022

# 10 Valores inteiros positivos
a = int(input('Valor 1: '))
b =  int(input('Valor 2: '))
c =  int(input('Valor 3: '))
d = int(input('Valor 4: '))
e = int(input('Valor 5: '))
f = int(input('Valor 6: '))
g =  int(input('Valor 7: '))
h =  int(input('Valor 8: '))
i = int(input('Valor 9: '))
j = int(input('Valor 10: '))
#média dos valores 
média = (a + b + c + d + e + f + g + h + i + j) / 10
print('A média entre {},{},{},{},{},{},{},{},{},{} é igual {}'.format(a, b, c, d, e, f, g, h, i, j, média))
#Menor valor selecionado
if média < 5:
    print('Média baixa'.format(média))
#Maior valor selecionado
if média > 5:
    print('Média alta'.format(média))
    
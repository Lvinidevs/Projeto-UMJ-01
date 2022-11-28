# Disciplina : Algoritmos e Estrutura de dados
# Professor(a) : Nathalia Menezes
# Descrição    :  Terceiro problrma fase 2
# Alunor(a)    : Lucas Vinicius da Silva
# Matricula    :  2022206348
# Data atual   :  21/10/2022

#coletar dados
# O para feminino e 1 para masculino
for c in range(1, 6):
    a = int(input("Sexo: "))
    b = int(input("idade: "))
    t = float(input("Altura: "))
print('Dados coletados {},{},{}'.format(a, b, t, c))
        
# Média da idade do grupo coletado
x = int(input('Valor 1: '))
y =  int(input('Valor 2: '))
z =  int(input('Valor 3: '))
d = int(input('Valor 4: '))
e = int(input('Valor 5: '))
média = (x + y + z + d + e) / 5
print('Média das idades {}'.format(média))

#Média de altura
a1 = float(input("Altura: "))
a2 = float(input("Altura: "))
a3 = float(input("Altura: "))
a4 = float(input("Altura: "))
a5 = float(input("Altura: "))
media = (a1 + a2 + a3 + a4 + a5) / 5
print('Média das alturas {}'.format(media))

#Média da idade dos homens
h1 = int(input("idade h1: "))
h2 = int(input("idade h2: "))

mda = (h1 + h2) /2
print('Média de idada dos homens {}'.format(mda))
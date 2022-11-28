# Disciplina   : Algoritmos e Estrutura de dados
# Professor(a)   :  Nathalia Menezes
# Descrição   : Leitor de temperatura 
# Autor(a)    : Lucas Vinicius da Silva
# Matricula   : 2022206348
# Data atual  :  21/10/2022

#Converter de Celsius(°C) para Kelvin(K)
K = float(input("C°: "))
cv =  (K + 273.15)
print('resultado {}'.format(cv))

#Converter de Fahrenheit(°F) para Kelvin(K)
K1 = float(input("F°: "))
cv1 = (K1 -32)*5/9+273.15
print('resultado {}'.format(cv1))

#Converter de Fahrenheit(°F) para Celsius(°C)
f = float(input("C°: "))
cv2 = (f -32)*5/9 
print('resultado {}'.format(cv2))

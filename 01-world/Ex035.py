#Desenvolva um programa que leia o comprimento de 3 retas e diga ai usuário se elas podem ou não formar um triângulo
print ('\33[0:35:40m-='*20)
print ('Analisador de Triângulos\033[m')
r1 = float(input('Digite o valor do primeiro triangulo: '))
r2 = float(input('Digite o valor do segundo triangulo:'))
r3 = float(input('Digite o valor do terceiro triangulo: '))
if r1 < r2 + r3 and r1 < r3 + r2 and r3 < r1 + r2:
    print ('Os segmentos acima podem formar um triângulo')
else:
    print ( 'Os segmentos acima não podem formar triângulo')


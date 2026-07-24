#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento
#Para salários superiores a R$1250,00, calcule um amumento de 10%
#Para salários inferiores ou iguais o aumento é de 15%

salarioantigo = float(input('Que salario analisar? '))
if salarioantigo <= 1250:
    salarionovo = (salarioantigo *15/100) + salarioantigo
else:
    salarionovo = (salarioantigo *10/100) + salarioantigo
print ('O novo salário é {}'.format(salarionovo))


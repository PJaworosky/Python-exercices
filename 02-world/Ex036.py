#Escreva um programa para aprovar o empréstimo para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstino será negado.

casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos = int(input('Em quantos anos você pretende pagar? '))
prestacao = casa / (anos * 12)
print ('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
minimo = salario * 30/100
if prestacao <= minimo:
    print ('O empréstimo foi CONCEDIDO ')
else:
    print ('Empréstimo NEGADO')


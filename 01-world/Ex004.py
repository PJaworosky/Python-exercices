#Programa que lê algo no teclado e mostre na tela o seu tipo prmitivo e todas as informações possíveis sobre ele
#Pra mostrar tipos primitivos: Usar type
a=input('Digite algo ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiscúla?', a.isupper())
print('Está em minúsculo?', a.islower())
print('Está capitalizada?', a.istitle())



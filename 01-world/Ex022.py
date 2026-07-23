#Crie um programa que leia um nome completo de uma pessoa e mostre O nome com letras maiúsculas e minúsculas. Qtas letras e qtas letras tem o primerio nome
nome= input('Digite seu nome completo: ').strip()
print ('Analisando seu nome...')
print ('Seu nome em maiúsculas é...')
print(nome.upper())
print ('Seu nome em minúsculas é...')
print(nome.lower())
print ('O nome tem {} letras'.format(len(nome)-nome.count(' ')))
print ('O primeiro nome tem {} letras'.format(len(nome.split()[0])))



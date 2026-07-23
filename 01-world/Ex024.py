#Crie um programa que leia um nome de uma cidade e diga se ela começa ou não com o nome "santo"
cid =  str(input('Digite o nome da cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')


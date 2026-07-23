# ----------------------------------------
# Exercise 029 - Speed Radar
# Curso em Vídeo - Python
# Author: Paloma Jaworosky
# ----------------------------------------

#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80 km/h, mostre uma msg dizendo que ele foi multado
#A multa vai custar R$7,00 por cada km acima do limite

velocidade = input('\33[32mQual a velocidade atual do carro? ')
velocidade = int(velocidade)
multa = int(velocidade - 80) *7
if velocidade > 80:
    print('\33[0;30;41mVocê excedeu o limite de velocidade de 80km/h\33[m')
    print(' \33[1mO valor da multa será R$ {:.2f}'.format(multa))
    print('\33[0;36mTenha um bom dia! DIRIJA COM SEGURANÇA!')

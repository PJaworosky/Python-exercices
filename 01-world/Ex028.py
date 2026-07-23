#Escreva um programa que faça o computadpr pensar em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir o número escolhido pelo computador
#O programa deverá escrever na tela se o usuário perdeu ou venceu
import random
from time import sleep #pra parecer que o computador está pensando
número= random.randint(1,5) #importei randomint pra pegar números inteiros
palpite= int(input('Advinhe um número entre 1 e 5: '))
print('PENSAND0...')
sleep(2)
if palpite == número:
    print('PARABÉNS, você acertou!')
else:
    print('Você errou! Eu pensei no número {} e não no número {}'.format(número, palpite))

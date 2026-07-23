#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno. cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O seno deste ângulo é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}" .format(seno, cosseno, tangente))

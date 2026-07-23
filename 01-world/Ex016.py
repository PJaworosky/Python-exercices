# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.#
import math
num= float(input("Digite um número "))
print("O valor digitado é {} e a sua porção inteira é {}".format(num,math.trunc(num)))
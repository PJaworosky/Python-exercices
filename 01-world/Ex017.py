# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
co=float(input("Digite o comprimento do CO "))
ca=float(input("Digite o comprimento do Ca "))
hi=math.hypot(co,ca)
print("O valor da hipotenusa é" , hi)

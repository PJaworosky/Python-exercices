# Um professor quer sortear um de seus quatro alunos para apagar o quadro.Faça um programa que leia o nome dos alunos e mostre o nome do escolhido
import random

n1= str(input("Nome do aluno 1 "))
n2= str(input("Nome do aluno 2 "))
n3= str(input("Nome do aluno 3 "))
n4= str(input("Nome do aluno 4 "))
lista = [n1,n2,n3,n4]
escolhido= random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))
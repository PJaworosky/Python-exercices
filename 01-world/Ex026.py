#Faça um programa que leia uma frase no teclado e mostre no final:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez
frase= str(input('Digite uma frase: ')).strip().upper()
print= str(input('A letra A aparece {} vezes na frase'.format(frase.count('A'))))
print= str(input('Ela aparece a primeira vez na posição {}.'.format(frase.find('A')+1)))
print= str(input('E aparece a última vez na posição {}'.format(frase.rfind('A')+1)))
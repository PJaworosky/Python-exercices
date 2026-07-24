#Desenolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem cobrando R$0.50 por km pra viagens de até 200km
# E R$0,45 para viagens mais longas

distancia = float(input(' Qual foi a distância da sua viagem? '))
resultado1 = distancia * 0.50
resultado2 = distancia * 0.45
if distancia <= 200:
    print(' A passagem sairá R${}'.format(resultado1))
else:
    print('A passagem sairá R${}'.format(resultado2))

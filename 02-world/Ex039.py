#Alsitamento militar
from datetime import date
ano= date.today().year
nascimento= int(input('Digite o ano do seu nascimento: '))
idade= ano - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, ano))
if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade < 18:
    print('Você ainda não tem 18 anos. Ainda faltam {} anos.'.format(18 - idade))
elif idade > 18:
    print('Você já deveria ter se alistado ')

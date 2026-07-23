#Informar quantas latas de tintas são necessárias para limpar a parede
l=(float(input('Digite a largura da parede: ')))
al=float(input('Digite a altura da parede: '))
área=l*al
print('Sua parede tem a dimensão de {} X {} e sua área é {:.2f} m2'.format(l,al,área))
latas=área/2
print('Para pintar esta parede você precisará de {} latas de tintas'.format(latas))




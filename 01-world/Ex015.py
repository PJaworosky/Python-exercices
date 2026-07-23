dias=int(input('Quantos dias o carro foi alugado?'))
km=float(input('Quantos km rodado?'))
pago= (dias*60) + (km*0.15)
print('O total a pagar é {}'.format(pago))

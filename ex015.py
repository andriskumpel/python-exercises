dias = int(input('Quantos dias foi alugado? '))
km = float(input('Quantos km foram rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(pago))
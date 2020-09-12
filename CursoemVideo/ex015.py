dias = int(input('Quantidade de dias rodados: '))
km = float(input('Digite a quantidade de km rodados: '))

resultado = (dias * 60) + (km * 0.15)

print('O total gasto foi de {:.2f} R$' . format(resultado))
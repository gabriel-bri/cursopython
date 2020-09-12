km = float(input('Digite a quantidade de quilômetros: '))

if km <= 200:
    print('Você pagará 0.50/km.')
    print('Sua passagem terá um valor de : {:.2f}'.format(km * 0.50))
else:
    print('Você pagará 0.40/km')
    print('Sua passagem terá um valor de : {:.2f}'. format(km * 0.45))
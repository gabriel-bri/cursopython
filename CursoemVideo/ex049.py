print('{:=^20}'.format(' TABUADA '))

numero = int(input('Digite um número para ver a tabuada: '))

print('=' * 15)
for c in range(0, 11):
    print('{} x {:2} = {:2}' .format(numero, c, numero * c))
print('=' * 12)
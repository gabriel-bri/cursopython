numero = int(input('Digite um número: '))
soma = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        soma += 1

if soma == 2:
    print('O número {} é primo' .format(numero))

else:
    print('O número {} não é primo' .format(numero))

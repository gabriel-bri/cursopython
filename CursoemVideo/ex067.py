
while True:
    numero_tabuada = int(input('Digite o número para ver a tabuada: '))

    if numero_tabuada < 0:
        break

    c = 0

    while c <= 10:
        print('{} x {} = {}'.format(numero_tabuada, c, numero_tabuada * c))
        c+= 1
print('Programa tabuada sendo encerrado...')
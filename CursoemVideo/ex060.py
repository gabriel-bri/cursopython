numero = int(input('Digite um número para saber o fatorial: '))

fatorial = 1

c = numero
print('Calculando {}! = ' .format(numero), end='')
while c > 0:
    fatorial *= c
    c -= 1
    print('{}' .format(c + 1), end='')
    print(' x ' if c >= 1 else ' = ', end='')
print('{}' .format(fatorial))
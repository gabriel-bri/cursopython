numero = 1
soma = 0
contador = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))

    if numero != 999:
        contador += 1
        soma += numero

    else:
        print('Encerrando programa...')

print('Você digitou {} números e a soma foi igual a {} ' .format(contador, soma))
maiorPeso = 0
menorPeso = 0

for c in range(0, 5):
    peso = float(input('Digite o seu peso: '))

    if c == 1:
        maiorPeso = peso
        menorPeso = peso

    else:
        if peso > maiorPeso:
            maiorPeso = peso

        if peso < menorPeso:
            menorPeso = peso

print('O maior peso encontrado foi {}, e o menor peso encontrado foi {}' .format(maiorPeso, menorPeso))
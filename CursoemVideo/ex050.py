soma = 0
for c in range(1, 7):
    numero = int(input("Digite o {}º valor: " .format(c)) )

    if numero % 2 == 0:
        soma += numero

print('A soma deu um total de {}' .format(soma))
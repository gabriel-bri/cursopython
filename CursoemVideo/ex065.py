op = ''
numero = media = qtdNumeros = maior = menor = somaNumeros = 0
while op in 'Ss':
    numero = int(input('Digite um número: '))
    op = str(input('Quer continuar? [S/N]')).upper().strip()[0]

    qtdNumeros += 1
    somaNumeros += numero

    if qtdNumeros == 1:
        maior =  menor = numero

    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

print('Foram digitados {} números, e a média entre os números foram de {}'
      .format(qtdNumeros, somaNumeros / qtdNumeros))
print('O maior valor foi: {}. E o menor valor foi: {}' .format(maior, menor))
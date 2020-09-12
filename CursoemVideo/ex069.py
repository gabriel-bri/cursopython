qtd18 = qtdHomem = qtdMulher20 = 0

while True:
    print('{:=^20}'.format(''))
    print('CADASTRE UMA PESSOA')
    print('{:=^20}'.format(''))

    idade = int(input('Digite a idade da pessoa: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]

    print('{:=^20}'.format(''))

    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if idade > 18:
        qtd18 += 1

    if sexo in 'M':
        qtdHomem += 1

    if idade < 20 and sexo in 'F':
        qtdMulher20 += 1

    if continuar in 'N':
        break
print('Fim do programa')
print('Total de pessoas com mais de 18: {} pessoas' . format(qtd18))
print('Total de homens cadastrados: {} homens' . format(qtdHomem))
print('Total de mulheres com menos de 20 anos: {} mulheres' . format(qtdMulher20))
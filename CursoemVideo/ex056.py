mediaIdade = 0
maisVelho = 0
nomeMaisVelho = ''
qtdMulheres = 0

for c in range(1, 5):

    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa: [M/F]'))

    mediaIdade += idade

    if c == 1 and sexo in 'Mm':
        maisVelho = idade
        nomeMaisVelho = nome

    if idade > maisVelho and sexo in 'Mm':
        maisVelho = idade
        nomeMaisVelho = nome

    if idade < 20 and sexo in 'Ff':
        qtdMulheres += 1


print('A média de idade do grupo é {}' .format(mediaIdade / 4))
print('O homem mais velho é {} com a idade de {} ' .format(nomeMaisVelho, maisVelho))
print('A quantidade de mulheres com idade menor de 20 são: {}' .format(qtdMulheres))
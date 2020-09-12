from datetime import date

qtdMaior = 0
qtdMenor = 0
anoAtual = date.today().year

for c in range(0, 7):
    anoNascimento = int(input('Digite o ano de nascimento: '))


    saldoIdade = abs(anoAtual - anoNascimento)

    if saldoIdade < 21:
       qtdMenor += 1

    else:
        qtdMaior += 1

print('''Existem {} maiores idades.
E existem {} menores de idade''' .format(qtdMaior, qtdMenor))
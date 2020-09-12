salario = float(input('Digite o salário: '))

if salario > 1250:
    aumento = (10 / 100 * salario)
    print('O novo salário agora é de: {}'.format(aumento + salario))
else:
    aumento = (15 / 100 * salario)
    print('O novo salário agora é de: {}'.format(aumento + salario))

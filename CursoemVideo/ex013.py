salario = float(input('Digite o salário: '))

aumento = (15 / 100 * salario)

print('Salário antigo: {}\n'
      'Salário com o aumento: {}'
      .format(salario, salario + aumento))
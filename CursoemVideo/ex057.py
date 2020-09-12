sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()

print('O sexo informado é: {}' .format(sexo))

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

op = 0

while op != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')
    op = int(input('Digite sua opção: '))
    if op == 1:
        print('Opção selecionada: [{}]' .format(op))
        print('A soma entre {} e {} é igual a {}: ' .format(n1, n2, n1 + n2))

    elif op == 2:
        print('Opção selecionada: [{}]' .format(op))
        print('A multiplicação entre {} e {} é igual a {}: ' .format(n1, n2, n1 * n2))

    elif op == 3:
        print('Opção selecionada: [{}]' .format(op))
        print('Entre {} e {} o maior número é {}: ' .format(n1, n2, max(n1, n2)))

    elif op == 4:
        print('Opção selecionada: [{}]' .format(op))
        print('Novos números...')
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))

    elif op == 5:
        print('Opção selecionada: [{}]'.format(op))
        print('Saindo do programa')

    else:
        print('Opção inválida, tente novamente!')
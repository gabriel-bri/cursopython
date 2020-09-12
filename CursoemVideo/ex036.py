valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
quantidadeAnos = int(input('Digte a quantidade de anos para pagar: '))

prestacaoMensal = valorCasa / (quantidadeAnos * 12)

porcentagem = (30 / 100 * salario)

print('Você terá uma prestação de: {:.2f}'.format(prestacaoMensal))
print('Verificando a disponibilidade do seu empréstimo...')

if prestacaoMensal <= porcentagem:
    print('Empréstimo aprovado')
else:
    print('Empréstimo reprovado')
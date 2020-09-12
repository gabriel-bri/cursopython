velocidade = float(input('Digite sua velocidade: '))

if velocidade > 80:
    print('MULTADO! EXCESSO DE VELOCIDADE')
    print('Você recebeu uma multa de: {:.2f}' .format((velocidade - 80) * 7.00))
else:
    print('Você está dentro dos limites de velocidade')
dinheiro = float(input('Digite a quantidade de dinheiro: '))

print('Com {} R$ você pode ter até: '
      '{:.2f} US$ '. format(dinheiro, dinheiro / 3.27))
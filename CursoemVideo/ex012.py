preco_produto = float(input('Digite o preço do produto: '))

desconto = (5 / 100 * preco_produto)

print('Preço antigo: {} \n'
      'Preço novo: {:.2f}'
      .format(preco_produto,
      preco_produto - desconto))
cont = qtdProdutosMil = totalCompra = menorProdutoPreco = 0
NomeProdutoBarato = ''

while True:
    nome_produto = str(input('Digite o nome do produto: ')).upper().strip()
    preco_produto = float(input('Digite o preço do produto: '))

    cont += 1
    totalCompra += preco_produto

    if cont == 1:
        menorProdutoPreco = preco_produto
        NomeProdutoBarato = nome_produto

    if preco_produto < menorProdutoPreco:
        menorProdutoPreco = preco_produto
        NomeProdutoBarato = nome_produto

    if preco_produto > 1000:
        qtdProdutosMil += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Desejar continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break
print('Foram comprados {} produtos ' . format(cont))
print('O total das compras foi de: {}' .format(totalCompra))
print('O menor produto foi: {}, por um total de {} reais ' .format(NomeProdutoBarato, menorProdutoPreco))
print('Foram comprados {} produtos acima de mil reais ' .format(qtdProdutosMil))
print('A médias das compras foi de: {:.2f}' .format(totalCompra / cont))

from time import sleep
valorProduto = float(input('Digite o preço do produto: '))

#sleep(2)

print("{:=^30}".format('FORMA DE PAGAMENTO'))
print('''[ 1 ] - à vista no dinheiro ou cheque'
[ 2 ] - à vista no cartão de crédito
[ 3 ] - em até 2x no cartão
[ 4 ] - 3x ou mais no cartão''')

condicaoPagamento = int(input('Digite a opção: \n '))

if condicaoPagamento == 1:
    print('Desconto de 10%')
    resultado = valorProduto - (10 / 100 * valorProduto)

elif condicaoPagamento == 2:
    print('Desconto de 5%')
    resultado = valorProduto - (5 / 100 * valorProduto)

elif condicaoPagamento == 3:
    parcela = valorProduto / 2
    print('Sua compra será parcelada em 2x de {:.2f} R$ SEM JUROS' .format(parcela))

elif condicaoPagamento == 4:
    totParcelas = int(input('Digite o total de parcelas: '))
    resultado = valorProduto + (20 / 100 * valorProduto)
    print('Sua compra será parcelada em {}x COM JUROS' . format(totParcelas), end='')
    print('com parcelas de {:.2f}' .format(resultado / totParcelas))

else:
    resultado = valorProduto
    print('Opção inválida, tente novamente')
print('Você pagará um valor de: {:.2f}' .format(resultado))

import math
dinheiro = int(input('Digite o valor a ser sacado: '))

quantidade50 = math.floor(dinheiro / 50)
quantidade20 = math.floor(dinheiro / 20)
quantidade10 = math.floor(dinheiro / 10)
quantidade1 = math.floor(dinheiro / 1)

if dinheiro >= 50:


print(dinheiro, quantidade50, quantidade20, quantidade10, quantidade1)


frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = '' .join(palavras)

inverso = junto[::-1]
print('Você digitou a frase -> {} ' .format(frase))

if inverso == junto:
    print('Temos um palíndromo')

else:
    print('A frase digitada não é um palíndromo')

'''
# You can use of this two ways to resolve this problem
frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = '' .join(palavras)

#inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
    
if inverso == junto:
    print('Temos um palíndromo')

else:
    print('A frase digitada não é um palíndromo')
'''
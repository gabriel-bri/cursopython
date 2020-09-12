frase = str(input('Digite uma frase: ')).strip().upper()

quantas_vezes = frase.upper().count('A')
posicao_inicial = frase.upper().find('A') + 1
posicao_final = frase.upper().rfind('A') + 1

print('A letra A apareceu {} vezes '.format(quantas_vezes))
print('Posição inicial: {}'.format(posicao_inicial))
print('Posição final: {}'.format(posicao_final))
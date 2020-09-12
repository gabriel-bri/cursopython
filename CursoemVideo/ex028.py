from random import randint
from time import sleep

mensagem = "JOGO DA ADVINHAÇÃO"
print("{:=^50}" . format(mensagem))

numero = int(input('Adivinhe o número: '))
maquina_numero = randint(0, 5)

print('PROCESSANDO...')
sleep(3)

print('Seu chute: {}'.format(numero))
print('O do computador: {} '.format(maquina_numero))

if numero == maquina_numero:
    print('PARABÉNS! Você venceu!')
else:
    print('PUTS! Você perdeu :/')

print('FIM DE JOGO')
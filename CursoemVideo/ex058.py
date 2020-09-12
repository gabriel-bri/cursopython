from random import randint
from time import sleep

tentativas = 0

mensagem = "JOGO DA ADVINHAÇÃO"
print("{:=^50}" . format(mensagem))

maquina_numero = 0
numero = 1
while numero != maquina_numero:
    numero = int(input('Adivinhe o número ente 0 e 10: '))
    maquina_numero = randint(0, 10)

    print('PROCESSANDO...')
    sleep(3)

    print('Seu chute: {}'.format(numero))
    print('O do computador: {} '.format(maquina_numero))

    if numero == maquina_numero:
        print('PARABÉNS! Você venceu!')
    else:
        tentativas += 1
        print('PUTS! Você perdeu :/')

print('FIM DE JOGO')
print('Você teve que fazer {} tentativas para conseguir vencer o jogo!' .format(tentativas))
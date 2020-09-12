from random import randint

print('{:=^30}' .format(''))
print('{:^30}' .format('VAMOS JOGAR PAR OU ÍMPAR?'))
print('{:=^30}' .format(''))

contador_vitorias = 0

while True:
    numero_usuario = int(input('Digite um valor: '))
    opcao_usuario = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    while opcao_usuario not in 'PI':
        opcao_usuario = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    numero_maquina = randint(0, 10)

    resultado = numero_maquina + numero_usuario

    if resultado % 2 == 0:
        mensagem = 'PAR'

    elif resultado % 2 == 1:
        mensagem = 'IMPAR'

    print('=*' * 15)
    print('Você jogou {} e o computador {}. Total de {} DEU {}' .
          format(numero_usuario, numero_maquina, resultado, mensagem))
    print('=*' * 15)

    if mensagem[0] != opcao_usuario:
        print('Você perdeu!')
        print('{:«^20}' .format(''))
        print('GAME OVER! Você venceu {} vezes.' .format(contador_vitorias))
        break

    else:
        print('Você venceu!')
        print('Vamos jgar novamente...')
        print('{:«^20}' .format(''))
        contador_vitorias += 1
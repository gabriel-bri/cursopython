from time import sleep
from random import randint

print('{:=^25}'.format('JOKENPO GAME'))

# Aqui faz a entrada de dados por parte do usuário
print('''[ 1 ] para PEDRA'
[ 2 ] para PAPEL
[ 3 ]para TESOURA\n''')

valorUsuario = int(input('Digite a sua opção: '))

if valorUsuario == 1:
    opcaoUsuario = 'PEDRA'

elif valorUsuario == 2:
    opcaoUsuario = 'PAPEL'

elif valorUsuario == 3:
    opcaoUsuario = 'TESOURA'

else:
    opcaoUsuario = 'TESOURA'

# A partir daqui a máquina gera um número aleatório e
# atribui esse valor ao seu tipo

print('Huuuummmm, deixa eu pensar...')
sleep(3)

valorMaquina = randint(1, 3)

if valorMaquina == 1:
    opcaoMaquina = 'PEDRA'

elif valorMaquina == 2:
    opcaoMaquina = 'PAPEL'

else:
    opcaoMaquina = 'TESOURA'

# Aqui verifica quem ganhou...
print('Computador jogou: {}' .format(opcaoMaquina))
print('Sua jogada: {}' .format(opcaoUsuario))
sleep(2)

if (opcaoUsuario == 'PAPEL' and opcaoMaquina == 'PEDRA') or (opcaoUsuario == 'TESOURA' and opcaoMaquina == 'PAPEL') or (opcaoUsuario == 'TESOURA' and opcaoMaquina == 'PEDRA'):
    print('Uau! Você me venceu!')
    print('Parabéns! \º/')

elif (opcaoMaquina == 'PAPEL' and opcaoUsuario == 'PEDRA') or (opcaoMaquina == 'TESOURA' and opcaoUsuario == 'PAPEL') or (opcaoMaquina == 'TESOURA' and opcaoUsuario == 'PEDRA'):
    print('Aaaa, que pena!')
    print('Eu venci você hahaha!')

else:
    print('Empate :/')
from time import sleep

sleep(3)
print('{:=^20}'. format(''))
print('{:^20}'.format('MENU'))
print('[ 1 ] para binário')
print('[ 2 ] para octal')
print('[ 3 ] para hexadecimal')

numero = int(input('Digite um número: '))
opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    print('{} convertido em binário é igual a {}' .format(numero, bin(numero)[2:]))

elif opcao == 2:
    print('{} convertido em octal é igual a {}' .format(numero, oct(numero)[2:]))

elif opcao == 3:
    print('{} convertido em hexadecimal é igual a {}' .format(numero, hex(numero)[2:]))

else:
    print('Opção inválida, tente novamente')
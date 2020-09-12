from time import sleep

print('-=-'*15)
print('         ANALISADOR DE TRIÂNGULOS            ')
print('-=-'*15)
sleep(3)

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1+r2 > r3 and r2+r3 > r1 and r3+r1 > r2:
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')
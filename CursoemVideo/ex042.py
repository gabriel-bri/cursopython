r1 = float(input('Digite o primeiro lado: '))
r2 = float(input('Digite o segundo lado: '))
r3 = float(input('Digite o terceiro lado: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r2 > r1:
    print('É possível fazer um triângulo')
    if r1 == r2 == r3:
        print('Triângulo equilátero')

    elif r1 != r2 != r3 != r1:
        print('Triângulo escaleno')

    else:
        print('Triângulo isósceles')
else:
    print('Não é possível formar um triângulo')
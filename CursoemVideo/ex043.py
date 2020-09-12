peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = (peso / pow(altura, 2))

print('O seu IMC é de: {:.1f}' .format(imc))

if imc < 18.5:
    print('Abaixo do peso')

elif imc >= 18.5 and imc < 25:
    print('Peso ideal')

elif imc >= 25 and imc < 30:
    print('Sobrepeso')

elif imc >= 30 and imc <= 40:
    print('Obesidade')

else:
    print('Obesidade mórbida')

from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo: '))

print('Com um ângulo de {}, obtemos:\n'
      'Seno de: {:.2f}\n'
      'Cosseno de: {:.2f}\n'
      'Tangente de: {:.2f}\n'
      .format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
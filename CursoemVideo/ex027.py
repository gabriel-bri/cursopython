nome = str(input('Digite seu nome: ')).strip()

quebra = nome.split()

print('Prazer em te conhecer: {}' . format(nome))
print('Seu primeiro nome é: {}' .format(quebra[0]))
print('Seu último nome é: {} '.format(quebra[len(quebra) - 1]))
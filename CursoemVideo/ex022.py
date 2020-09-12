nome = str(input('Digite um nome: ')).strip()

print("""Seu nome em maiúsulo: {}
Seu nome em minísculo: {}
Quantas letras? {}
Quantas letras no primeiro nome? {}
""" .format(nome.upper(), nome.lower(),
            len(nome)-nome.count(' '), nome.find(' ') ))
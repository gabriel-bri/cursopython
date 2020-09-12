from datetime import date

anoNascimento = int(input('Digite o ano de nascimento: '))
sexo = str(input('Digite o seu sexo M ou F: '))
anoAtual = date.today().year

idade = anoAtual - anoNascimento

if 'M' in sexo.upper():
    print('Você precisa realizar o alistamento obrigatório...')
    if idade < 18:
        saldo = abs(idade - 18)
        print('Ainda vai se alistar')
        print('Faltam {} anos para o seu alistamento'.format(saldo))
        print('Seu alistamento será em {} '.format(anoAtual + saldo))
    elif idade == 18:
        print('Já é hora de se alistar')
    else:
        saldo = abs(idade - 18)
        print('Já passou do tempo de se alistar')
        print('Você está atrasado em {} anos com o serviço militar!'.format(saldo))
        print('Seu alistamento deveria ter sido feito em {} '.format(anoAtual - saldo))

else:
    print('Você não precisa fazer o alistamento obrigatório')
cidade = str(input('Digite o nome de sua cidade: ')).strip()

verifica = 'SANTO' in cidade[0:5].upper()

print('Tem SANTO? {}' .format(verifica))
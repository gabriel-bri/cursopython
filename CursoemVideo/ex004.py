n = input('Digite qualquer coisa: ')
print('O tipo é {} ' .format(type(n)))
print('É numérico ? {} ' . format(n.isnumeric()))
print('É alfanumérico ? {} ' .format(n.isalpha()))
print('É letra maior ? {} ' .format(n.islower()))
print('É um digito ? {} ' .format(n.isdigit()))
print('É um espaço ? {} ' .format(n.isspace()))
print('É um título ? {} ' .format(n.istitle()))
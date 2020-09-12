metros = float(input('Digite o valor em metros: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm =  metros * 100
mm =  metros * 1000

print('O valor {} em quilômetros é igual a {}'. format(metros, km))
print('O valor {} em hectômetros é igual a {}'. format(metros, hm))
print('O valor {} em decâmetro é igual a {}'. format(metros, dam))
print('O valor {} em decímetros é igual a {}'. format(metros, dm))
print('O valor {} em centímetros é igual a {}'. format(metros, cm))
print('O valor {} em milímetros é igual a {}'. format(metros, mm))
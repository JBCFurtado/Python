print('Conversor de moedas')
print('e = Euros')
print('d = Dollar')
print('m = Pesos Mexicanos')
print('a = Pesos Argentinos')
print('l = Libras')
moeda = input('Qual a moeda?: ')
reais = float(input('Quantos em reais você gostaria de converter? '))
if reais <0: print('Quantidade inválida')
elif moeda == 'e': print(reais*0.2132196162, 'Euros')
elif moeda == 'd':
    print(reais*0.24630541871, 'Dólares')
elif moeda == 'm':
    print(reais*4.7619047619, 'Pesos Mexicanos')
elif moeda == 'a':
    print(reais*9.0909090909, 'Pesos Argentinos')
elif reais == 'l':
    print(moeda*0,20366598778, 'Libras')
else:
    print('Moeda inválida')
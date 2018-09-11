#Ano bissexto
ano = int(input('Informe o ano: '))
if ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0:
    print('O ano é Bissexto!')
else:
    print('O ano NÃO é Bissexto')
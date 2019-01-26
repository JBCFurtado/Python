#CARDÁPIO CALÓRICO
print('Escolha seu Prato na tabela abaixo')
print('1 - Vegetariano')
print('2 - Peixe')
print('3 - Frango')
print('4 - Carne')
prato = int(input('Digite o prato escolhido: '))
print('Escolha sua Sobremesa na tabela abaixo: ')
print('1 - Abacaxi')
print('2 - Sorvete diet')
print('3 - Mousse diet')
print('4 - Mousse chocolate')
sobremesa = int(input('Digite a sobremesa escolhida: '))
print('Escolha sua Bebida na tabela abaixo: ')
print('1 - Chá')
print('2 - Suco de laranja')
print('3 - Mousse diet')
print('4 - Mousse chocolate')
bebida = int(input('Digite a bebida escolhida: '))

if (prato != '1' and prato != '2' and prato != '3' and prato != '4') or \
        (sobremesa != '1' and sobremesa != '2'and sobremesa != '3' and sobremesa != '4') or \
        (bebida != '1' and bebida != '2' and bebida != '3' and bebida != '4'):
    print('Escolha inválida!.')
else:
    if prato == '1':
        caloria1 = 180
    if prato == '2':
        caloria1 = 230
    if prato == '3':
        caloria1 = 250
    if prato == '4':
        caloria1 = 350
    opt1 = caloria2
    if sobremesa == '1':
        caloria2 = 75
    if sobremesa == '2':
        caloria2 = 110
    if sobremesa == '3':
        caloria2 = 170
    if sobremesa == '4':
        caloria2 = 200
    opt2 = caloria3
    if bebida == '1':
        caloria3 = 20
    if bebida== '2':
        caloria3 = 70
    if bebida == '3':
        caloria3 = 100
    if bebida == '4':
        caloria3 = 65
    opt3 = caloria3
    soma = (opt1 + opt2 + opt3)
    print('O total de calorias da refeição escolhida e: {0} cal.'.format(soma))
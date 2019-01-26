cedula1 = 1
cedula2 = 10
cedula3 = 50
valor_compra = int(input('Digite o valor da compra: '))
valor_dinheiro = int(input('Digite o valor do dinheiro: '))
troco = abs(valor_compra - valor_dinheiro)
troco1 = troco // cedula3
troco_resto = troco % cedula3
troco2 = troco_resto // cedula2
troco3 = troco_resto % cedula2
print('\nTroco: ', troco)
print('\nNúmeros de cédulas abaixo:')
print(troco1, 'Cédulas de 50 reais')
print(troco2, 'Cédulas de 10 reais')
print(troco3, 'Cédulas de 1 real')
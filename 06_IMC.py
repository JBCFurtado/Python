#IMC
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
imc = peso / (altura ** 2)
print('Seu IMC é: %.2f' % imc)
if imc < 16.0:
    print('Magreza grave')
elif imc < 17.0:
    print('Magreza moderada')
elif imc < 18.5:
    print('Magreza leve')
elif imc < 25.0:
    print('Saudável')
elif imc < 30.0:
    print('Sobrepeso')
elif imc < 35.0:
    print('Obesidade grau I')
elif imc < 40.0:
    print('Obesidade grau II ou Severa)')
else:
    print('Obesidade grau III ou Mórbida)')
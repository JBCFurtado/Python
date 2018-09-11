#Classificação de nadadores
idade = int(input('Qual a idade do participante? '))
if idade <5:
    print('Classificação inválida')
elif idade <= 7:
    print('Infantil A')
elif idade <= 10:
    print('Infantil B')
elif idade <= 14:
    print('Juvenil A')
elif idade <= 17:
    print('Juvenil B')
else:
    print('Adulto')
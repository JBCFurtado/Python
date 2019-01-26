total = 0
quantidade = int(input('Quantos números: '))
for i in range(quantidade):
    numero = float(input('Digite um numero: '))
    total += numero
print('média é : ', total/quantidade)
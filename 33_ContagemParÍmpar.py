cont_impar = 0
cont_par = 0
num = int(input("Entre com um número [999 para encerrar]: "))
while (num != 999):
    num = int(input("Entre com um número [999 para encerrar]: "))
    if (num % 2 == 0):
        cont_par += 1
    else:
        cont_impar += 1
print('Contagem dos pares:', cont_par)
print('Contagem dos impares:', cont_impar)
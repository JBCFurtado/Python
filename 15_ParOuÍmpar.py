#Par ou Ímpar
numero = float(input('Digite um número que te direi se é par ou impar: '))
resto = numero % 2
if resto == 0:
    print('O número digitado é Par.')
else:
    print('O número digitado é Ímpar.')
#01-Exercise
#Somatório dos N primeiros números definido pelo usuário.')
def somatorio(n):
    soma = 0
    for i in range(n+1):
        soma += i
    return soma
x = int(input('Digite um valor: '))
resultado = somatorio(x)
print('\nO somatório dos {0} primeiros números é {1}'.format(x, resultado), '.')


soma = 0
cont = 0
for c in range(0, 5, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores é {}'.format(cont, soma))
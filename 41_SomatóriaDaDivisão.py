resultado = 0
valor= int(input('Insira qualquer valor: '))
print()
def soma ():
    return (i/((i*2)-1))
for i in range(1, valor+1):
    print('{0}/{1} = {2}'. format(i, (i*2)-1,soma()))
    resultado += soma()
print('\nA soma da divisão é =', resultado)
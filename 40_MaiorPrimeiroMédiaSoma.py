L = []
a = 0
b = 0
c = 0
print('ATENÇÃO!!!!!!!!!!!!!!!')
print('Digite 999 para parar!')
while b != 999:
    a += 1
    b = int(input('\tDigite qualquer valor: '))
    if b == 999:
        break
    if b < 0:
        def Num_Negativo():
            return (b)
        c += Num_Negativo()
    L.append(b)
def Num_Maximo():
    return (max(L))
def Num_Soma():
    return (sum(L))
def Primeiro_Num():
    return (L[0])
def Result_Media():
    return (Num_Soma() / (a - 1))
print('\nO maior valor digitado foi =', Num_Maximo())
print('O primeiro número digitado foi =', Primeiro_Num())
print('A média é =', Result_Media())
print('A soma dos números foi =', Num_Soma())
print('A soma dos números negativos é =', c)
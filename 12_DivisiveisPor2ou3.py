#Divisíveis por 2 ou 3
n1 = int(input(' Digite o valor de n1 : '))
n2 = int(input(' Digite o valor de n2 : '))
n3 = int(input(' Digite o valor de n3 : '))
n4 = int(input(' Digite o valor de n4 : '))
if (n1 % 2 == 0 or n1 % 3 == 0) and (n2 % 2 == 0 or n2 % 3 == 0) \
        and (n3 % 2 == 0 or n3 % 3 == 0) and (n4 % 2 == 0 or n4 % 3 == 0):
    print(n1, n2, n3, n4)
elif (n1 % 2 == 0 or n1 % 3 == 0) and (n2 % 2 == 0 or n2 % 3 == 0) \
        and (n3 % 2 == 0 or n3 % 3 == 0):
    print(n1, n2, n3)
elif (n1 % 2 == 0 or n1 % 3 == 0) and (n2 % 2 == 0 or n2 % 3 == 0) \
        and (n4 % 2 == 0 or n4 % 3 == 0):
    print(n1, n2, n4)
elif (n1 % 2 == 0 or n1 % 3 == 0) and (n3 % 2 == 0 or n3 % 3 == 0) \
        and (n4 % 2 == 0 or n4 % 3 == 0):
    print(n1, n3, n4)
elif (n2 % 2 == 0 or n2 % 3 == 0) and (n3 % 2 == 0 or n3 % 3 == 0) \
        and (n4 % 2 == 0 or n4 % 3 == 0):
    print(n2, n3, n4)
elif (n1 % 2 == 0 or n1 % 3 == 0) and (n2 % 2 == 0 or n2 % 3 == 0):
    print(n1, n2)
elif (n1 % 2 == 0 or n1 % 3 == 0) and (n3 % 2 == 0 or n3 % 3 == 0):
    print(n1, n3)
elif (n1 % 2 == 0 or n1 % 3 == 0) and (n4 % 2 == 0 or n4 % 3 == 0):
    print(n1, n4)
elif (n2 % 2 == 0 or n2 % 3 == 0) and (n3 % 2 == 0 or n3 % 3 == 0):
    print(n2, n3)
elif (n2 % 2 == 0 or n2 % 3 == 0) and (n4 % 2 == 0 or n4 % 3 == 0):
    print(n2, n4)
elif (n3 % 2 == 0 or n3 % 3 == 0) and (n4 % 2 == 0 or n4 % 3 == 0):
     print(n3, n4)
elif n1 % 2 == 0 or n1 % 3 == 0:
    print(n1)
elif n2 % 2 == 0 or n2 % 3 == 0:
    print(n2)
elif n3 % 2 == 0 or n3 % 3 == 0:
    print(n3)
elif n4 % 2 == 0 or n4 % 3 == 0:
    print(n4)
else:
    print('Os números digitados acima não são divisíveis por 2 ou 3.')
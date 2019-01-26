#Raízes de um polinômio
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
delta = (b**2 - 4*a*c)**(1/2)
x1 = (-b+delta)/(2*a)
x2 = (-b-delta)/(2*a)
print(x1)
print(x2)


#QUESTÃO 2
a = int(input('Digite primeiro valor: '))
b = int(input('Digite segundo valor: '))
c = int(input('Digite terceiro valor: '))
if(c < b):
        result = c
        c = b
        b = result
if(b < a):
        result = b
        b = a
        a = result
if(c < b):
        result = c
        c = b
        b = result
print(a, b, c)
if (a == b)or(a == c)or(b == c):
    print("Obs.: existem números iguais!")
    print('')
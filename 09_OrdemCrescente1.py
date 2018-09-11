#Ordem crescente
a = int(input("Digite primeiro valor: "))
b = int(input("Digite segundo valor: "))
c = int(input("Digite terceiro valor: "))
if (a>b)and(a>c):
        if b>c:
          print (c, b, a)
        else:
          print (b, c, a)
if (b>a)and(b>c):
        if a>c:
          print (c, a, b)
        else:
          print (a, c, b)
if (c>a)and(c>b):
        if a>b:
          print (b, a, c)
        else:
          print (a, b, c)
if (a==b)or(a==c)or(b==c):
        print("Obs.: existem numeros iguais!")
        print('')
#Apresentar o menor e o maior valor iformado
a = int(input('Digite o 1º número. '))
b = int(input('Digite o 2º número. '))
c = int(input('Digite o 3º número. '))
d = int(input('Digite o 4º número. '))
e = int(input('Digite o 5º número. '))

menor = a
if b <= a and b <= c and b <= d and b <= e:
    menor = b
if c <= a and c <= b and c <= d and c <= e:
    menor = c
if d <= a and d <= b and d <= c and d <= e:
    menor = d
if e <= a and e <= b and e <= c and e <= d:
    menor = e
maior = a
if b >= a and b >= c and b >= d and b >= e:
    maior = b
if c >= a and c >= b and c >= d and c >= e:
    maior = c
if d >= a and d >= b and d >= c and d >= e:
    maior = d
if e >= a and e >= b and e >= c and e >= d:
    maior = e

if (a == b and a == c and a == d and a == e) and (b == a and b == c and b == d and b == e) \
        and (c == a and c == b and c == d and c == e) and (d == a and d == b and d == c and d == e) \
        and (e == a and e == b and e == c and e == d):
    print('Todos valores são iguais.')

else:
    print('O menor valor digitado é: {}'.format(menor))
    print('O maior valor digitado é: {}'.format(maior))
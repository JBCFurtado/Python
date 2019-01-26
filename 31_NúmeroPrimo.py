primos = []
num = int(input('Qual numero testar? '))
for n in range(1, num+1):
    if num % n == 0:
        primos.append(n)
    if len(primos) > 2:
        print('O número {} NÃO é Primo!'.format(num))
        break
if len(primos) == 2:
    print('O número {} é PRIMO.'.format(num))
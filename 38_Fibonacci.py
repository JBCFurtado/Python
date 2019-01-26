def fibonacci():
    l = []
    n = 1
    n1 = 1
    l.append(n)
    l.append(n1)
    x = int(input('Digite o numero:'))
    for i in range(2, x):
        l.append(n + n1)
        n1 = l[i]
        n = l[i - 1]
    return(l)
print(fibonacci())
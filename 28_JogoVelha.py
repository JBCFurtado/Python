titulo = 'Jogo da velha'
linha1 = '—' * 30
linha2 = '·' * 40
print()
print(linha1.center(40))
print(titulo.center(40))
print(linha1.center(40))
print()

l1 = ['a', 'b', 'c']
l2 = ['d', 'e', 'f']
l3 = ['g', 'h', 'i']

la1 = ['?', '?', '?']
la2 = ['?', '?', '?']
la3 = ['?', '?', '?']


def velha():
    print()
    print('A|B|C')
    print('—————')
    print('D|E|F')
    print('—————')
    print('G|H|I')
    print()
    print('OBS: Digite a letra em MINÚSCULO!'.center(40))


def loop(a, m):
    if m == l1[i]:
        l1[i] = a
        la1[i] = l1[i]
    else:
        if m == l2[i]:
            l2[i] = a
            la2[i] = l2[i]
        else:
            if m == l3[i]:
                l3[i] = a
                la3[i] = l3[i]


def tela(a):
    print('{0}|{1}|{2}'.format(a[0], a[1], a[2]).center(40))


def horizontal(a):
    if l1[a] and l1[a + 1] and l1[a + 2] == jogador1:
        print()
        return (jogador1)
    elif l2[a] and l2[a + 1] and l2[a + 2] == jogador1:
        print()
        return (jogador1)
    elif l3[a] and l3[a + 1] and l3[a + 2] == jogador1:
        print()
        return (jogador1)


print()
x = input('Digite o nome do jogador 1: ')
y = input('Digite o nome do jogador 2: ')
print()

print(linha1.center(40))
jogador1 = input('{0} Escolha seu Simbolo! '.format(x).center(40))
jogador2 = input('{0} Escolha seu Simbolo! '.format(y).center(40))
print(linha1.center(40))

print('\n{0} = {1}    {2} = {3}\n'.format(x, jogador1, y, jogador2).center(40))

velha()

print()
while 1 != 0:
    m = input('Vez do {0}: '.format(x))
    n = input('Vez do {0}: '.format(y))
    for i in range(3):
        loop(jogador1, m)
        loop(jogador2, n)

    print()
    tela(la1)
    print('___'.center(40))
    tela(la2)
    print('———————'.center(40))
    tela(la3)

    if horizontal(0) == jogador1:
        print('Vencedor {0}'.format(x))
        break
    elif horizontal(0) == jogador2:
        print('Vencedor {0}'.format(y))
        break
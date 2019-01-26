titulo = 'Jogo da Advinhação!'
linha = '-' * 28
linha1 = "_" * 40
linha2 = '—' * 50
y = 1
print(linha)
print(titulo.center(25))
print(linha)
print()
usuario = input('\t\tDigite seu nome: ')

print('\t\tBem Vindo {0} ao Jogo!'.format(usuario))

print()
print(linha1.center(20))
print('Digite (0) FACIL (1) MEDIO (2) DIFICIL!'.center(20))
x = int(input('Qual sua dificuldade? '))
print(linha1.center(20))
print()


def funcao(a, b, c, d, e):
    from random import randint
    y = randint
    h = (y(0, 10 * b))
    pontos = 1000 * b
    print('Seus pontos = ', pontos)

    for i in range(d):
        print()
        c = int(input('Diga qual o seu chute: '))
        if c > h:
            pontos -= a
            print('Seu poder de Advinhação está muito fraco, tente NOVAMENTE!')
            print('Numero chutado MAIOR que o numero secreto')
        elif c < h:
            pontos -= a
            print('Seu poder de Advinhação está muito fraco, tente NOVAMENTE!')
            print('Numero chutado MENOR que o numero secreto')
        else:
            print()
            print(linha2)
            print('Parabéns {0} jovem gafanhoto! Número acertado!'.format(usuario))
            print(linha2)
            print('{0} Você fez: {1} pontos '.format(e, pontos))
            break


while y != 0:
    if x == 0:
        funcao(100, 1, 0, 10, usuario)
    elif x == 1:
        funcao(150, 10, 0, 15, usuario)
    else:
        funcao(250, 100, 0, 20, usuario)

    print()
    y = int(input('Quer continuar {0} vacilão? (0)NÃO e (1)SIM: '.format(usuario)))
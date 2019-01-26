titulo = 'JOGO DA FORCA'
linha1 = '←' * 10
linha2 = '→' * 10
linha3 = '—' * 30
linha4 = '*' * 26
linha5 = '←' * 42
linha6 = '→' * 42

chancesLimite = 0
chances = 1
l = 0

from random import randint

y = randint

print()
print(linha1, end= '')
print(linha2)
print(titulo.center(22))
print(linha2, end='')
print(linha1)
print()

nome = input('Digite seu nome : ')

print()
print(linha5.center(20))
print('Digite (0) FACIL (1) MEDIO (2) DIFICIL!'.center(20))
dificuldade = int(input('Qual sua dificuldade? '))
print(linha6.center(20))
print()

fruta = ['maca', 'laranja', 'uva', 'banana']
letras = []

x = y(fruta.index(fruta[0]), fruta.index(fruta[len(fruta) - 1]))
palavraSecreta = fruta[x]
print(palavraSecreta)

if dificuldade == 0:
    chancesLimite = 16
elif dificuldade == 1:
    chancesLimite = 10
else:
    chancesLimite = 8

chute = 0

while chances <= chancesLimite:
    z = 0

    print()
    print('\nVocê tem {0} chute de {1}!'.format(chances, chancesLimite))
    chances += 1
    letra = input('\n\t\tDigite uma letra: ')

    print()
    for i in range(len(palavraSecreta)):
        if letra == palavraSecreta[i]:
            print(linha3.center(40))
            print('Acertou, posição {0}!'.format(i + 1).center(40))
            z += 1
            l += 1
    if z != 0:
        chances -= 1
        print(linha3.center(40))
    if z == 0:
        print(linha3.center(40))
        print('{0} Você Errou!'.format(nome).center(40))
        print(linha3.center(40))

    for i in range(len(letras)):
        if letra == letras[i]:
            print()
            print('Você já chutou essa letra ANIMAL!')
            print('Preste atenção no que está fazendo!')
            chances -= 1
            letras.remove(letra)
    if letras.count(letra) > 1:
        l -= z
    chute = letra
    letras.append(chute)

    print()
    print('Letras chutadas: ', end='')
    for i in range(len(letras)):
        print(letras[i], end='')
    if l == len(palavraSecreta):
        print('\nParabéns {0} Jovem gafanhoto completou a palavra!'.format(nome))
        break
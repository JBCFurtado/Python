linha = '-' * 50
titulo = 'ALGORITMOS E TÉCNICAS DE PROGRAMAÇÃO \nProfessora: Vanderlene Rocha\n3ª Avaliação\nAluno: Josué Batista'
print(linha)
print(titulo.center(50))
print(linha)
linha = '-' * 50
titulo = '01_Somatório dos N primeiros números'
print(linha)
print(titulo.center(50))
print(linha)

def somatorio():
    a = 0
    n = int(input('Digite o numero: '))
    for i in range(n + 1):
        a += i
    return a
print('Soma dos números =', somatorio())
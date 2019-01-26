#Média com codição da quinta nota
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
nota4 = float(input('Digite sua quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/4
if (media >= 7):
    print('Aprovado, sua média é: ', media)
nota_exame = float(input('Digite sua quinta nota: '))
nova_media = (media + nota_exame) / 2
if (nova_media >= 5):
    print('Aprovado em exame, sua média é: ', nova_media)
else:
    print('Reprovado, sua média é: ', nova_media)

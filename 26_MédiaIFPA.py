#MEDIA IFPA
linha = '-' * 60
titulo = 'INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PARÁ \nCampus Altamira\nAUTOR: Jobs-TI'
print(linha)
print(titulo.center(60))
print(linha)
linha = '-' * 60
titulo = 'MÉDIA DE APROVAÇÃO'
print(linha)
print(titulo.center(60))
print(linha)
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2
if media >= 7:
    print('PARABÉNS!!! Aprovado, sua média é: ', media)
elif media < 7:
    print('Sua média foi', media)
    nota_exame = float(input('Infelizmente você NÃO atingiu a media 7. \nPor favor Digite a nota da RECUPERAÇÃO: '))
    nova_media = (media + nota_exame) / 2
    if nova_media >= 7:
        print('PARABÉNS !!! Aprovado em exame, sua média é: ', nova_media)
    else:
        print('REPROVADO, sua média é: ', nova_media)
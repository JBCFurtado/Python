print('Nota geral de um edital')
qualidade = int(input('Qual a nota para a Qualidade: '))
preco = int(input('Qual a nota para o Preço?: '))
prazo = int(input('Qual a nota para o Prazo?: '))
nota_geral1 = (qualidade + preco + prazo)/3
nota_geral2 = (qualidade + preco + prazo)/3
if qualidade < 7:
    nota_geral = 0
    print('Nota Geral é: ', nota_geral)
else:
    if preco >= 7:
        print('Nota geral é: ',nota_geral1)
    else:
        print('Nota geral é: ',nota_geral2)
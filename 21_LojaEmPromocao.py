#Loja em promoção
print('PROMOÇÕES DO DIA EM TODA NOSSA LOJA!')
print('AVISTA: 9% DE DESCONTO!')
print('EM 5X: SEM DESCONTO E NEM JUROS')
print('EM 10X ACRÉSCIMO DE 17% DE JUROS')
comp = float(input('Qual o valor da compra? '))
desconto =comp-(comp*9)/100
normal = comp/5
anormal = (comp+(comp*17)/100)/10
print('Preço à vista com desconto: ',desconto)
print('Sem juros em: 5x',normal)
print('Ou em 10x de:', anormal)

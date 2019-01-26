def prestacao():
    valor = int(input('Digite o preço: '))
    taxa = int(input('Digite o valor da taxa: '))
    tempo = int(input('Digite o tempo em meses de atraso: '))
    prestacao = valor + (valor*(taxa/100)*tempo)
    return(prestacao)
print(prestacao())
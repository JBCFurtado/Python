print('Informe os valores para os lados do triângulo!')
lado1 = int(input('Qual o valor do lado 1? '))
lado2 = int(input('Qual o valor do lado 2? '))
lado3 = int(input('Qual o valor do lado 3? '))
if lado1 >= lado2 + lado3 \
    or lado2 >= lado1 + lado3 \
    or lado3 >= lado2 + lado1:
    print('Os lados NÃO formam um trângulo.')
else:
    print('Os lados FORMAM um triângulo.')

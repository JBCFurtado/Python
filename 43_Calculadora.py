# Calculadora de C pra Python

print("\t\t\t#########################")
print("\t\t\t#Welcome the Calculation#")
print("\t\t\t#########################\n")
print()

x = 1

while x != 0:
    escolha = input("Digite a operaçao selecionada: ")
    if escolha == '#':
        num1 = float(input("Digite o numero do radicando: "))
        num2 = float(input("Digite o numero do indice da raiz: "))
    else:
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite um segundo numero: "))
    print()

    soma = (num1 + num2)
    subtracao = (num1 - num2)
    multiplicacao = (num1 * num2)
    divisao = (num1 / num2)
    rest_div = (num1 % num2)
    potencia = (num1 ** num2)
    raiz = num1 ** (1 / num2)

    if (escolha == '+'):
        print("A soma de %.1f com %.1f e igual a %.4f " % (num1, num2, soma))
    elif (escolha == '-'):
        print("A subtraçao de %.1f com %.1f e igual a %.1f " % (num1, num2, subtracao))
    elif (escolha == '*'):
        print("A multiplicaçao entre %.1f e %.1f e igual a %.1f " % (num1, num2, multiplicacao))
    elif (escolha == '/'):
        print("A divisao entre %.1f e %.1f e igual a %.1f " % (num1, num2, divisao))
    elif (escolha == '%'):
        print("O resto da divisao de %.1f e %.1f e igual a %.1f" % (num1, num2, rest_div))
    elif (escolha == '**'):
        print("A potencia entre %.1f e %.1f e igual a %.1f" % (num1, num2, potencia))
    elif (escolha == '#'):
        print("Raiz do radicando %.1f e indice da raiz %.1f e igual a %.1f" % (num1, num2, raiz))

    elif (escolha == "help"):
        print()
        print("Sinais das operaçoes")
        print("Para somar use: '+'")
        print("Para subtrair use: '-'")
        print("Para multiplicar use: '*'")
        print("Para dividir use: '/'")
        print("Para obter o resto da divisao use: '%'")
        print("Para ter a potencia use: '**'")
        print("Para ter a raiz use: '#'")
        print("Para todas as operaçoes suportadas use: 'todas'")
        print()

    elif (escolha == "todas"):
        print("A soma de %.1f com %.1f e igual a %.1f " % (num1, num2, soma))
        print("A subtraçao de %.1f com %.1f e igual a %.1f " % (num1, num2, subtracao))
        print("A multiplicaçao entre %.1f e %.1f e igual a %.1f " % (num1, num2, multiplicacao))
        print("A divisao entre %.1f e %.1f e igual a %.1f " % (num1, num2, divisao))
        print("O resto da divisao de %.1f e %.1f e igual a %.1f" % (num1, num2, rest_div))
        print("A potencia entre %.1f e %.1f e igual a %.1f" % (num1, num2, potencia))
        print("Raiz do radicando %.1f e indice da raiz %.1f e igual a %.1f" % (num1, num2, raiz))
    else:
        print("Voce nao digitou uma operaçao valida, se quiser ajuda digite help no local da operaçao!")
        print()

    x = int(input('\n\t\t\tDeseja continuar a usar a calculadora?\n\t\t\tDigite(1)Sim ou Digite(0)Não:'))
    print()

print("Obrigado Por Usar Nossa Calculadora!")
#Condição nome
nome = (input('Digite seu nome: '))
sexo = (input('Digite seu sexo sendo: m = masculino e f = feminino. '))
if (sexo == "m"):
    print('Sr. ', nome)
elif (sexo == "f"):
        print('Sra. ', nome)
else:
    print('Sexo informado inválido')
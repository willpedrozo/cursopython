executar = True
while executar:
    escolhas = '''
            [1] ou [+] para Somar
            [2] ou [-] para Subtrair
            [3] ou [/] para Dividir
            [4] ou [*] para Multiplicar
            [5] para Sair
            '''
    print(escolhas)
    operador = input("Qual sua Opção?: ")
    valor1 = input("Qual é o primeiro valor?: ")
    valor2 = input("Qual é o segundo valor?: ")
    valor1 = int(valor1)
    valor2 = int(valor2)

    texto_sair = '''
        [1] Não, desejo sair!
        [2] Sim, desejo realizar outro calculo
    '''

    #Adição
    if operador == "1" or operador == "+" or operador == "Somar":
        resultado = valor1 + valor2
        print("O resultado da soma: " + str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar outro calculo? ")
        if operador == "1":
            executar = False
 

    #Subtração
    if operador == "2" or operador == "-" or operador == "Subtrair":
        resultado = valor1 - valor2
        print("o resultado da subtração: " + str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar ourto calculo? ")
        if operador == "1":
            executar = False
    #Divisão

    #Multiplicação

    #Sair



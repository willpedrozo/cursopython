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
    if operador == "5":
        print("Obrigado! ")
        executar = False
    else:
        valor1 = int(input("Qual é o primeiro valor?: "))
        valor2 = int(input("Qual é o segundo valor?: "))

        texto_sair = '''
            [1] Não, desejo sair!
            [2] Sim, desejo realizar outro calculo
        '''
        #Adição
        if operador == "1" or operador == "+" or operador == "Somar":
            resultado = str(valor1 + valor2)
            print(f'O resultado da soma: {resultado}')
            print(texto_sair)
            fim = input("Deseja realizar outro calculo? ")
            if fim == "1":
                print('Obrigado!')
                executar = False
            

        #Subtração
        if operador == "2" or operador == "-" or operador == "Subtrair":
            resultado = str(valor1 - valor2)
            print(f'O resultado da subtração: {resultado}')
            print(texto_sair)
            fim = input("Deseja realizar outro calculo? ")
            if fim == "1":
                print('Obrigado!')
                executar = False
            
        #Divisão
        if operador == "3" or operador == "/" or operador == "Dividir":
            resultado = str(valor1 / valor2)
            print(f'O resultado da divisão: {resultado}')
            print(texto_sair)
            fim = input("Deseja realizar outro calculo? ")
            if fim == "1":
                print('Obrigado!')
                executar = False
            

        #Multiplicação
        if operador == "4" or operador == "*" or operador == "Multiplicar":
            resultado = str(valor1 * valor2)
            print(f'O resultado da multiplicação: {resultado}')
            print(texto_sair)
            fim = input("Deseja realizar outro calculo? ")
            if fim == "1":
                print('Obrigado!')
                executar = False
            




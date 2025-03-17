from random import randint

print("####    Iniciando o Jogo de Adivinhar    ####")

objetivo = randint(0,100)
chances = 10
tentativa = 0

while tentativa != objetivo:
    tentativa = input(f'Chute um número entre 0 a 100: ')
    if tentativa.isnumeric():
        tentativa = int(tentativa)
        chances = chances - 1
        if tentativa == objetivo:
            print(f'')
            print(f'Parabéns, você venceu!! O número era {objetivo} e você ainda tinha {chances} chances! ')
            print(f'')
            break
        else:
            print(f'')
            if tentativa > objetivo:
                print(f'Você errou. Dica: é um número menor que {tentativa}')
            else:
                print(f'Você errou. Dica: é um número maior que {tentativa}')
            print(f'Você ainda possui {chances} chances. ')
            print(f'')
        if chances == 0:
            print(f'')
            print(f'Suas chances acabaram, você perdeu! ')
            print(f'')
            break

print("####    Fim de Jogo    ####")


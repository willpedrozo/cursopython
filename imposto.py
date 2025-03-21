'''def calculadora_ir(nome):
    print(f'Oi {nome}, me chamou? ')

calculadora_ir("William")'''

def calculadora_ir(salario_bruto):
    #tabela de aliquotas do imposto de renda
    tabela_ir = [
        {'faixa':(0, 1903.98), 'aliquota': 0, 'deducao': 0},
        {'faixa':(1903.99, 2826.65), 'aliquota': 7.5, 'deducao': 142.80},
        {'faixa':(2826.66, 3751.05), 'aliquota': 15, 'deducao': 344.80},
        {'faixa':(3751.06, 4664.68), 'aliquota': 22.5, 'deducao': 630.80},
        {'faixa':(4664.69, float('inf')), 'aliquota': 27.5, 'deducao': 860.80}
    ]
    #calcular o imposto
    imposto = 0
    for faixa in tabela_ir:
        if salario_bruto > faixa['faixa'][0] and salario_bruto < faixa['faixa'][1]:
            imposto = (salario_bruto * faixa['aliquota'] / 100) - faixa['deducao']
            break
    return imposto

salario = float(input(f'Informe seu salário mensal: '))
resultado_final = calculadora_ir(salario)
print(f'O imposto a ser pago é de R$ {resultado_final:.2f}')


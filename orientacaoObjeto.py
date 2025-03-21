class Carro:
    def __init__(self, modelo, cor):
        #atributos do carro
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento #+= substitui o exemplo de self.velocidade = self.velocidade + incremento. Diminuir usa o "-"
        print(f'O carro {self.modelo} acelerou para {self.velocidade} km/h')
    
        
    def parar(self):
        self.velocidade = 0
        print(f'O carro {self.modelo} parou.')

#criar o carro
meu_carro = Carro('Fusca', 'Azul')
carro_do_instrutor = Carro('Suzuki Jimmy', 'Amarelo')

#usar os métodos
meu_carro.acelerar(20) #aceleramos mais 20km/h
meu_carro.acelerar(30) #aceleramos mais 30km/h
meu_carro.parar()

carro_do_instrutor.acelerar(5)
carro_do_instrutor.parar()



import turtle
import random
import time

tela = turtle.Screen()
tela.title("Jogo da cobrinha")

pontos = 0

tela.bgcolor('black')
tela.setup(width=600, height=600)

tela.tracer(0)

#definições da cobra
cobra = turtle.Turtle()
cobra.speed(0)
cobra.shape("square")
cobra.color("green")
cobra.penup()
cobra.goto(0,0)
cobra.direction = 'stop'

#definições da comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.goto(0,100)

# comandos da cobra
def vai_pra_cima():
    cobra.direction = 'up'
def vai_pra_baixo():
    cobra.direction = 'down'
def vai_pra_esquerda():
    cobra.direction = 'left'
def vai_pra_direita():
    cobra.direction = 'right'

#fazer a cobra obedecer
tela.listen()
tela.onkeypress(vai_pra_cima, 'Up')
tela.onkeypress(vai_pra_baixo, 'Down')
tela.onkeypress(vai_pra_direita, 'Right')
tela.onkeypress(vai_pra_esquerda, 'Left')

# o coração do aplicativo ta aqui

while True:
        tela.update()
        if cobra.distance(comida) < 20:
             x = random.randint(-290,290)
             y = random.randint(-290,290)
             comida.goto(x,y)
             pontos += 10
             tela.title(f'Pontos: {pontos}')
        time.sleep(0.1)
        if cobra.direction == "right":
             x = cobra.xcor()
             cobra.setx(x + 20)
        elif cobra.direction == "left":
             x = cobra.xcor()
             cobra.setx(x - 20)
        elif cobra.direction == "up":
             y = cobra.ycor()
             cobra.sety(y + 20)
        elif cobra.direction == "down":
             y = cobra.ycor()
             cobra.sety(y - 20)
        if cobra.xcor()>290 or cobra.xcor()<-290 or cobra.ycor()>290 or cobra.ycor()<-290:
             tela.title(f'GAME OVER!! Sua pontação foi de {pontos}')
             cobra.goto(0,0)
             cobra.direction = 'stop'
                         
tela.mainloop()

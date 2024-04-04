import turtle

# Inicializa a janela da aplicacao
loadWindow = turtle.Screen()
# Inicializa a funcionalidade para desenhar na tela e configura seus dados
pen = turtle.Pen()
pen.speed()
pen.penup()
pen.goto(0, -100)
pen.pendown()

# Define uma função para desenhar um fractal de linhas
def drawFractalLine(length, depth):
    pen.forward(length)
    # Se a profundidade for maior que 1, desenha a linha fractal recursivamente
    if depth > 1:
        pen.backward(length / 2)
        pen.left(90)
        drawFractalLine(length / 2.1, depth - 1)
        pen.right(180)
        drawFractalLine(length / 2.1, depth - 1)
        pen.right(90)
        pen.forward(length / 2)
    # Volta para a posição original e desenha a linha novamente
    pen.right(180)
    pen.forward(length)

# Desenha uma linha fractal com comprimento 400 e profundidade 8
drawFractalLine(400, 8)
pen.right(180)
drawFractalLine(400, 8)

# Encerra o programa quando a janela é clicada
turtle.exitonclick()
import turtle

# configs da tela screen
WIDTH, HEIGHT = 1600, 900 # largura e altura
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)
screen.bgcolor('black')
screen.delay(0)

# configs do turtle
t = turtle.Turtle()
t.pensize(3) #grossura da linha
t.speed(0)
t.setpos(-WIDTH // 3, -HEIGHT // 2) # posição inicial da nossa "caneta"
t.color('red')

# configs do sistema l
# + vira a caneta para direita, e o menos para esquerda
# F, G desenha a linha

gens = 7 # geração
axiom = 'F'
chr_1, rule_1 = 'F', 'F-G+F+G-F'
chr_2, rule_2 = 'G', 'GG'

step = 8 # distancia que a caneta vai se mover em cada geração
angle = 120 # angulo de giro

def apply_rules(axiom):
    res = ''
    print(axiom)

    for chr in axiom:
        if chr == chr_1:
            res += rule_1
        elif chr == chr_2:
            res += rule_2
        else:
            res += chr

    return res

def aplly_gen(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return (axiom)


def draw_sierpinski(gens):
    initialAxiom = 'F'

    turtle.pencolor('white')
    turtle.goto(-WIDTH // 2 + 60, -HEIGHT // 2 - 100)
    turtle.clear()
    turtle.write(f'geração: {gens}', font=('ARIAL', 60))

    initialAxiom = aplly_gen(gens, initialAxiom)

    for chr in initialAxiom:
        if chr == chr_1 or chr == chr_2:
            t.forward(step)
        elif chr == '+':
            t.right(angle)
        elif chr == '-':
            t.left(angle)

    screen.exitonclick()

    return

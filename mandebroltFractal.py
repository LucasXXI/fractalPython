import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis

# Define uma função para gerar o conjunto de Mandelbrot
def mandelbrot():
    # Gera gera 2 eixos reais espaçados e com um numero de pontos definidos
    x = np.linspace(-2, 1, 3000)
    y = np.linspace(-1, 1, 2000)
    #adiciona os eixos complexos a partir da definicao abaixo
    c = x[:, newaxis] + 1j * y[newaxis, :]
    # Inicializa z como igual a c (para a iteracao)
    z = c

    # Itera um número definido de vezes para calcular o conjunto de Mandelbrot
    for i in range(100):
        # Realiza o loop no conjunto utilizando a funcao definida de Mandelbrot z = z^2 + c
        z = (z * z) + c

    # Verifica se o valor absoluto de z é menor que 2 (ou seja, se ele permanece limitado)
    conj = (abs(z) < 2)
    # Plota o conjunto de Mandelbrot
    plt.imshow(conj.T, extent=[-2, 1, -1, 1])
    plt.show()
import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis


def mandelbrot():
    x = np.linspace(-2,1,3000)
    y = np.linspace(-1,1,2000)
    c = x[:, newaxis] + 1j * y[newaxis, :]
    z = c

    for i in range(100):
        z = (z*z) + c

    conj = (abs(z) < 2)
    plt.imshow(conj.T, extent=[-2,1,-1,1])
    plt.show()

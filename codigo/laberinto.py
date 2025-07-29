import numpy as np
import matplotlib.pyplot as plt

def crear_laberinto():
    laberinto = np.array([
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ])
    return laberinto

def visualizar_laberinto(laberinto, camino=None):
    plt.imshow(laberinto, cmap='gray')

    if camino:
        for (x, y) in camino:
            plt.scatter(y, x, color='red')

    plt.xticks([]), plt.yticks([])
    plt.show()

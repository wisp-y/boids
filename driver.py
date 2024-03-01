from . import boids
import matplotlib.pyplot as plt

class Driver:
    def __init__(self):
        flock = boids.Boids(25, 0, 100, 0, 100, 0.01, 5)
        plt.scatter(flock.return_x_vals(), flock.return_y_vals())
        plt.show()
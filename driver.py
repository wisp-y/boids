from boids import Boids
import matplotlib.pyplot as plt
import numpy as np

class Driver:
    def __init__(self):
        min = 0
        max = 1000
        flock = Boids(50, min, max, min, max, -100, 100, 1000)
        plt.ion()
        figure, ax = plt.subplots(figsize=(10, 8))
        sc = ax.scatter(np.array([min, max]), np.array([min, max]))
        for i in range(100):
            flock.move_all_boids()
            sc.set_offsets(np.c_[flock.return_x_vals(), flock.return_y_vals()])
            figure.canvas.draw_idle()
            plt.pause(0.1)
        plt.waitforbuttonpress()
        

driver = Driver()
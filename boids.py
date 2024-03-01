from . import boid
import numpy as np

class Boids:
    def __init__(self, num_b, minX, maxX, minY, maxY, minV, maxV):
        self.boids = [boid.Boid(minX, maxX, minY, maxY, minV, maxV)] * num_b
    
    def move_all_boids(self):
        for boid in self.boids:
            r1_x = boid.centering()[0]
            r1_y = boid.centering()[1]
            r2_x = boid.distancing()[0]
            r2_y = boid.distancing()[1]
            r3_x = boid.matching()[0]
            r3_y = boid.matching()[1]

            boid.x_v = boid.x_v + r1_x + r2_x + r3_x
            boid.y_v = boid.y_v + r1_y + r2_y + r3_y

            boid.x = boid.x + boid.x_v
            boid.y = boid.y + boid.y_v
            
    def return_x_vals(self):
        values = []
        for boid in self.boids:
            values.append(boid.x)
        return np.array(values)
    
    def return_y_vals(self):
        values = []
        for boid in self.boids:
            values.append(boid.y)
        return np.array(values)
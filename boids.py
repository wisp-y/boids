from boid import Boid
import numpy as np
import math

class Boids:
    def __init__(self, num_b, minX, maxX, minY, maxY, minV, maxV, capV):
        self.boids = []
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.capV = capV
        for x in range(num_b):
            self.boids.append(Boid(minX, maxX, minY, maxY, minV, maxV))
    
    def move_all_boids(self):
        for boid in self.boids:
            closest = boid.find_boids_in_range(self.boids, (self.maxX - self.minX) / 2)
            closest2 = boid.find_boids_in_range(self.boids, (self.maxX - self.minX) / 10)
            r1_x = boid.centering(self.boids, closest)[0]
            r1_y = boid.centering(self.boids, closest)[1]
            r2_x = boid.distancing(self.boids)[0]
            r2_y = boid.distancing(self.boids)[1]
            r3_x = boid.matching(self.boids, closest2)[0]
            r3_y = boid.matching(self.boids, closest2)[1]

            boid.x_v = boid.x_v + r1_x + r2_x + r3_x
            boid.y_v = boid.y_v + r1_y + r2_y + r3_y

            if (boid.find_v_magnitude() > self.capV):
                boid.x_v /= boid.find_v_magnitude()
                boid.y_v /= boid.find_v_magnitude()

            boid.x = boid.x + boid.x_v
            boid.y = boid.y + boid.y_v

            if boid.x > self.maxX or boid.x < self.minX:
                boid.x = (boid.x % (self.maxX - self.minX)) + self.minX
            
            if boid.y > self.maxY or boid.y < self.minY:
                boid.y = (boid.y % (self.maxY - self.minY)) + self.minY
            
            
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
    

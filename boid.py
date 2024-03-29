import random
import math

class Boid:
    def __init__(self, minX, maxX, minY, maxY, minV, maxV):
        self.x = random.randrange(minX, maxX)
        self.y = random.randrange(minY, maxY)
        self.x_v = random.randrange(minV, maxV)
        self.y_v = random.randrange(minV, maxV)
    
    def update_position(self, x, y):
        self.x = x
        self.y = y
    
    def update_vel(self, x, y):
        self.x_v = x
        self.y_v = y

    def centering(self, boids, closest):
        p_x = 0
        p_y = 0
        for boid in boids:
            if boid != self and boid in closest:
                p_x += boid.x
                p_y += boid.y
        p_x /= len(boids) - 1
        p_y /= len(boids) - 1

        ret = [(p_x - self.x) / 100, (p_y - self.y) / 100]
        return ret
    
    def distancing(self, boids):
        p_x = 0
        p_y = 0
        for boid in boids:
            if boid != self:
                if self.find_distance(boid) < 25:
                    p_x -= (boid.x - self.x)
                    p_y -= (boid.y - self.y)

        ret = [p_x, p_y]
        return ret
    
    def matching(self, boids, closest):
        p_x_v = 0
        p_y_v = 0
        for boid in boids:
            if boid != self and boid in closest:
                p_x_v += boid.x_v
                p_y_v += boid.y_v
        p_x_v /= len(boids) - 1
        p_y_v /= len(boids) - 1

        ret = [(p_x_v - self.x_v) / 4, (p_y_v - self.y_v) / 4]
        return ret

    def find_distance(self, boid):
        return math.sqrt((self.x - boid.x) * (self.x - boid.x) + (self.y - boid.y) * (self.y - boid.y))
    
    def find_v_magnitude(self):
        return math.sqrt(self.x_v * self.x_v + self.y_v * self.y_v)
    
    def find_boids_in_range(self, boids, range):
        closest = []
        for boid in boids:
            if boid != self:
                if (self.find_distance(boid) < range):
                    closest.append(boid)
        return closest
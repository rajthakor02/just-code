import turtle
import math
import random

def setup_enviroment():
    screen = turtle.Screen()
    screen.bgcolor("#000000")
    screen.title("Ultimate Love")
    screen.tracer(0)
    return screen

class VortexParticle:
    def __init__(self):
        self.reset()
        self.history = [(self.x, self.y)] * 5

    def reset(self):
        self.x = random.uniform(-400, 400)
        self.y = random.uniform(-300, 300)
        self.vx = random.uniform(-2,2)
        self.vy = random.uniform(-2,2)
        self.color_base = random.random()
        self.target_angle = random.uniform(0, 2 * math.pi)

    def update(self, t, mouse_x, mouse_y):
        self.history.append((self.x, self.y))
        self.history.pop(0)
        scale = 15 + 3 * math.sin(t * 0.03)
        heart_x = 16 * math.sin(self.target_angle)**3 * scale
        heart_y = (13 * math.cos(self.target_angle) - 5 * math.cos(2*self.target_angle) - 2 * math.cos(3*self.target_angle) - math.cos(4*self.target_angle)) * scale
        dx, dy = heart_x - self.x, heart_y - self.y
        dist = math.sqrt(dx**2 + dy**2)
        self.vx += dx * 0.002
        self.vy += dy * 0.002
        self.vx += -dy * 0.001
        self.vy += dx * 0.001



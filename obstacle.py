import pygame
import random

# Constants
posX = random.randint(100, 800)
posY = random.randint(100, 500)

class Obstacle:
    def __init__(self):
        self.color = (0, 0, 0)
        self.width = random.randint(50, 100)
        self.height = random.randint(50, 100)
        self.x = posX
        self.y = posY
        self.vel_x = random.choice([-0.5,0.5])
        self.vel_y = random.choice([-0.5,0.5])

    def update_position(self, x, y):
        self.x += self.vel_x
        self.y += self.vel_y

        # Bounce off walls
        if self.x <= 0 or self.x + self.width >= 900:
            self.vel_x *= -1
        if self.y <= 0 or self.y + self.height >= 600:
            self.vel_y *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

import pygame
import random

class healthItem:
    def __init__(self):
        self.color = (0, 255, 0)  # Green color for health item
        self.width = random.randint(20, 50)
        self.height = random.randint(20, 50)
        self.x = random.randint(0, 900 - self.width)
        self.y = random.randint(0, 600 - self.height)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x + self.width // 2, self.y + self.height // 2), self.width // 2)

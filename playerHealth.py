import pygame

class PlayerHealth:
    def __init__(self, initial_health=100):
        self.health = initial_health
        self.max_health = initial_health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def draw_health_bar(self, screen, x, y, width=500, height=10):
        pygame.draw.rect(screen, (255, 0, 0), (x, y, self.health * 2000 // width, height)) 
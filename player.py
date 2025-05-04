import pygame

class Player:
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius
        self.x = 0
        self.y = 0

    def update_position(self):
        self.x, self.y = pygame.mouse.get_pos()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def change_color(self, new_color):
        self.color = new_color

    def check_collision(self, obstacles):
        for obstacle in obstacles:
            if (self.x - self.radius < obstacle.x + obstacle.width and
                self.x + self.radius > obstacle.x and
                self.y - self.radius < obstacle.y + obstacle.height and
                self.y + self.radius > obstacle.y):
                return True
        return False

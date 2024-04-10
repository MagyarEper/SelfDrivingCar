import pygame
import Controls

class Car:
    def __init__(self, x, y, width, height, color=('blue')) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.controls = Controls

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            (
                self.x - self.width/2,
                self.y - self.height/2,
                self.width,
                self.height,
            )
        )

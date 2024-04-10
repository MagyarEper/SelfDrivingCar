import pygame

class Controls:
    def __init__(self):
        self.forward = False
        self.left = False
        self.right = False
        self.reverse = False
    
    def inputKeyDown(self, key):
        if key == pygame.K_LEFT:
            self.left = True
        elif key == pygame.K_RIGHT:
            self.right = True
        elif key == pygame.K_UP:
            self.forward = True
        elif key == pygame.K_DOWN:
            self.reverse = True

    def inputKeyUp(self, key):
        if key == pygame.K_LEFT:
            self.left = False
        elif key == pygame.K_RIGHT:
            self.right = False
        elif key == pygame.K_UP:
            self.forward = False
        elif key == pygame.K_DOWN:
            self.reverse = False
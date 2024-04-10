import pygame
import Car

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Self Driving Car")
clock = pygame.time.Clock()
running = True

DARKGRAY = (169,169,169)

while running:
    screen.fill("gray")
    road = pygame.Rect(430, 0, 430, 1280)
    car = Car.Car(640,360,60,100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            # car.controls.Controls.inputKeyDown(event.key)
                

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("Space key released")




    pygame.draw.rect(screen, DARKGRAY, road)
    car.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
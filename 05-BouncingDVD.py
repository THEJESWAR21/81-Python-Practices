import pygame, random
pygame.init()

screen = pygame.display.set_mode((1280,720))
framerate = pygame.time.Clock()
running = True
deltatime = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    pygame.display.flip()


pygame.quit()


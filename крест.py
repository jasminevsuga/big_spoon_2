import pygame

def draw():
    pygame.init()
    a = input().split()
    a = [int(i) for i in a]
    tt = width, height = a[0], a[1]
    screen = pygame.display.set_mode(tt)
    pygame.draw.line(screen, (255, 255, 255), [0, 0], [width, height], 5)
    pygame.draw.line(screen, (255, 255, 255), [0, height], [width, 0], 5)


draw()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
pygame.guit()
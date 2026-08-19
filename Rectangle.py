import pygame

pygame.init()

sc=pygame.display.set_mode((400,300))
d=False

while not d:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            d=True
    pygame.draw.rect(sc,(0,125,255), pygame.Rect(30,30,160,60))  

    pygame.display.flip()

import pygame

pygame.init()

sc=pygame.display.set_mode((400,400))

sc.fill((255,255,255))
g=(130,105,120)

pygame.draw.circle(sc,g,(300,300),50)
pygame.draw.circle(sc,g,(100,100),50,3)

pygame.display.update()

r=True
while r:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            r=False

pygame.quit()
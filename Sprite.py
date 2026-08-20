import pygame


def main():
    pygame.init()

    sw, sh = 500, 400
    screen = pygame.display.set_mode((sw, sh))
    pygame.display.set_caption("Mini Sprite Adventure")

    x, y = 50, 50
    spw, sph = 60, 60
    spd = 4

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 125, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)

    cur = WHITE
    clk = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pr = pygame.key.get_pressed()

        if pr[pygame.K_LEFT]:
            x -= spd
        if pr[pygame.K_RIGHT]:
            x += spd
        if pr[pygame.K_UP]:
            y -= spd
        if pr[pygame.K_DOWN]:
            y += spd

        x = min(max(0, x), sw - spw)
        y = min(max(0, y), sh - sph)

        if x == 0:
            cur = BLUE
        elif x == sw - spw:
            cur = YELLOW
        elif y == 0:
            cur = RED
        elif y == sh - sph:
            cur = GREEN
        else:
            cur = WHITE

        screen.fill(BLACK)

        pygame.draw.circle(screen, GREEN, (420, 320), 35)
        pygame.draw.circle(screen, BLUE, (80, 320), 35, 4)

        srect = pygame.Rect(x, y, spw, sph)
        pygame.draw.rect(screen, cur, srect)

        pygame.display.flip()
        clk.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

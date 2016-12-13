import sys, pygame, circle, const, random

from circle import circle
from const import *
pygame.init()


ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

balls = []
c = circle((500, 500), (2, 2))
def rand_i(l, u):
    return random.randint(l, u)

for i in range(5):
    #balls.append(circle((100 * i, 100 * i),(2, 2)))
    (balls.append(circle((rand_i(50, 700),rand_i(50, 700)),(rand_i(-5,5),
        rand_i(-5,5)))))

#print(random.randint(0,10))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    SCREEN.fill(BLACK)
    #screen.blit(ball, ballrect)
    #pygame.draw.circle(screen, WHITE, (500, 500), 50, 0)
    for i in balls:
        i.update(balls)
        i.draw()

    pygame.display.flip()

main()

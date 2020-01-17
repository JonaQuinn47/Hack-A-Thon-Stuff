import sys, pygame
pygame.init()

size = width, height = 1000, 1000
speed = [1, 0]
colors = [(27, 0, 135), (176, 51, 26), (194, 92, 29), (227, 141, 36), (240, 191, 77)]

screen = pygame.display.set_mode(size)

ball = pygame.image.load("blopp.png")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(colors[4], (0, 0, 1000, 200))
    screen.fill(colors[3], (0, 200, 1000, 400))
    screen.fill(colors[2], (0, 400, 1000, 600))
    screen.fill(colors[1], (0, 600, 1000, 800))
    screen.fill(colors[0], (0, 800, 1000, 1000))

    screen.blit(ball, ballrect)
    pygame.display.flip()

    pygame.time.wait(1)
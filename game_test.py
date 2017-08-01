import pygame
from random import randint


clock = pygame.time.Clock()

color = (255,255,255)


pygame.init()
screen = pygame.display.set_mode((490, 490))
done = False
is_blue = True
x = 10
y = x
rect_size = 30

move = x + rect_size
border = x

gridx = []
gridy = []

for i in range(12):
    gridx.append(i)
    gridy.append(i)

print(gridx)
print(gridy)

def makeX_grid(randX):
    return (randX * 40 + 10)



while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True


        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] and y > border: y -= move
        if pressed[pygame.K_DOWN]and y < (screen.get_height() - move): y += move
        if pressed[pygame.K_LEFT] and x > border + rect_size/2: x -= move


        if pressed[pygame.K_RIGHT] and x < (screen.get_width() - (rect_size+border)): x += move

        pygame.draw.rect(screen, (255,0,0), pygame.Rect(makeX_grid(gridx[randint(0,11)]), y, rect_size, rect_size))

        screen.fill((0,0,0))

        print(x)

        pygame.draw.rect(screen, color, pygame.Rect(x, y, rect_size, rect_size))


        pygame.display.flip()
        clock.tick(10)

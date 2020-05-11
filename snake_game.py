from random import randint
import sys, pygame
pygame.init()

l_col = (0, 0, 0)
color = (255, 255, 255)

#size = (width, height)
size = (720, 600)
screen = pygame.display.set_mode(size)

screen.fill(color)
"""Draw lines"""
x = 0
while x <= 720:
        pygame.draw.line(screen, l_col, (x, 0), (x, 600))
        x = x + 20

y = 0
while y <= 600:
        pygame.draw.line(screen, l_col, (0, y), (720, y))
        y = y + 20
"""End of drawing lines"""
var_rect = []
var_rect.append(pygame.Rect(121, 121, 19, 19))

pygame.draw.rect(screen, (255, 0, 0), var_rect[0])

pygame.display.flip()

direction = [20, 0]
score = 0
food = pygame.Rect(521, 521, 19, 19)
create_food = 1
while 1:
        should_i_erase = 1
        pygame.time.delay(150-2*score)

        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                        print("Score: ", score)
                        pygame.display.quit()
                        sys.exit()
                elif e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_RIGHT and direction[0] != -20:
                                direction = [20, 0]
                        elif e.key == pygame.K_LEFT and direction[0] != 20:
                                direction = [-20, 0]
                        elif e.key == pygame.K_UP and direction[1] != 20:
                                direction = [0, -20]
                        elif e.key == pygame.K_DOWN and direction[1] != -20:
                                direction = [0, 20]

        var_rect.insert(0, var_rect[0].move(direction[0], direction[1]))
        var_rect[0][0] = var_rect[0][0]%720
        var_rect[0][1] = var_rect[0][1]%600

        for x in range(1, len(var_rect)):
                if var_rect[x] == var_rect[0]:
                        print("Score: ", score)
                        pygame.display.quit()
                        sys.exit()

        if var_rect[0] == food and create_food != 1:
                should_i_erase = 0
                score = score + 1
                create_food = 1

        if create_food == 1:
                food.left = 20 * randint(0, 35) + 1
                food.top = 20 * randint(0, 29) + 1
                create_food = 0

        if should_i_erase == 1:
                pygame.draw.rect(screen, (255, 255, 255), var_rect[-1]) #erase
                del var_rect[-1]
                

        pygame.draw.rect(screen, (255, 0, 0), var_rect[0])      #draw next one
        pygame.draw.rect(screen, (0, 255, 0), food)
        pygame.display.flip()

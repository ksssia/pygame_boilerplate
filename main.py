import random
import pygame
from constants import black, white, green, bright_green, display_height, display_width, car_width, clock, gameDisplay, carImg, fon
from functions import button, text_objects, things, car, things_dodged, crash
import datetime

pygame.init()


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("Don't crash my car", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    # car one pos.
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    # second car pos.
    x1 = (display_width * 0.65)
    y1 = (display_height * 0.8)


    x_change = 0
    x1_change = 0

    gameExit = False
    dodged = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100


    thingCount = 1


    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()

            # управление
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5



                elif event.key == pygame.K_a:
                    x1_change = -5
                elif event.key == pygame.K_d:
                    x1_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x1_change = 0




        # смена позиции
        x += x_change
        x1 += x1_change

        # фон
        gameDisplay.fill(white)
        gameDisplay.blit(fon, (0, 0))

        # дорожные помехи
        things(thing_startx, thing_starty)
        thing_starty += thing_speed

        # создаем машину
        car(carImg, x, y)
        car(carImg, x1, y1)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash(dodged)
        if x1 > display_width - car_width or x1 < 0:
            crash(dodged)

        # логика для счетчика
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)


        # логика для появления помех
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)

        if y < thing_starty + thing_height:
            #print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                #print('x crossover')
                crash(dodged)


        if y1 < thing_starty + thing_height:
            #print('y1 crossover')

            if x1 > thing_startx and x1 < thing_startx + thing_width or x1 + car_width > thing_startx and x1 + car_width < thing_startx + thing_width:
                #print('x1 crossover')
                crash(dodged)

        pygame.display.update()
        # кадры в секунду = 60
        clock.tick(60)


if __name__ == '__main__':
    game_intro()
    game_loop()
    pygame.quit()
    quit()
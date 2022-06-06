import random
import pygame
import sys
import time

from pygame.color import THECOLORS

#стартуем в файле модули пайгейм
pygame.init()

#размер окна
display_width = 800 # парамето высота
display_height = 600 # параметр ширина

# отрисовать окна игры
gameDisplay =  pygame.display.set_mode((display_width, display_height)) # размер
pygame.display.set_caption("Don't crush my car, dude!") #название

# цвета RGB
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# модуль для времени, чтобы мониторить кадры в секунду
clock = pygame.time.Clock()

# создаем игрока
carImg = pygame.image.load('image/8.png') # картинка для игрока
carImg = pygame.transform.scale(carImg, (70, 120)) # задаем размер картинки
car_width = 73

# отрисовкапрепятствий
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


#отрисовка авто
def car (x, y):
    gameDisplay.blit(carImg, (x, y))
#  обработка текста
def text_objects(text, font):
    textSurface = font .render(text, True, black)
    return textSurface, textSurface.get_rect()


# вывод текста на экран
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('You Crashed')

# блок (функция) для запуска игры
def game_loop():
    # размещение
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    # параметры для появления things
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 3
    thing_width = 100
    thing_height = 100

    x_change = 0 # позиция (смещение по иксу)
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()
            # блок для обработки нажатия на клавиши
            if event.type == pygame.KEYDOWN:
                # если нажали на esc, то окно закрывается
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
                    pygame.quit()

                if event.key == pygame.K_LEFT:
                    x_change = -5

                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            # условия для движения
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        # смена позиции
        x += x_change


        # фон
        gameDisplay.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed # скорость

        # создаем машину
        car (x, y)
        # задаем границы
        if x > display_width - car_width or x <0:
            gameExit = True
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
        #проверяем на обновления
        pygame.display.update()
        #кадры в секунду = 60
        clock.tick((60))

game_loop()
pygame.quit()
quit()
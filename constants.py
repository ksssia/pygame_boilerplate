from pygame import time, image, transform, display

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

# display_params
display_width = 800
display_height = 600

# car_settings
crashed = False
car_width = 73
car_speed = 0

# модуль для времени, чтобы мониторить кадры в секунду
clock = time.Clock()

carImg = image.load('image/7.png')  # картинка для игрока
carImg = transform.scale(carImg, (70, 80))  # задаем размер картинки, если большая
enemyImg = image.load('image/8.png') # enemy pic
enemyImg = transform.scale(enemyImg, (70, 80))
fon = image.load('image/fon.png')
fon = transform.scale(fon, (800, 600))


gameDisplay = display.set_mode((display_width, display_height))
display.set_caption("Don't crush my car, dude!")  # название игры


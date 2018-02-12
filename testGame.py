import pygame
import time
import random

pygame.init()

# colors
black = (0, 0, 0)
white = (255, 255, 255)

# display coordinates
display_width = 800
display_height = 600

# game display
pygame.display.set_caption('RACING GAME')
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

# Car Image
carImage = pygame.image.load('D:/Python/Python Project/Sample Images/racecar005.png')
car_width = 70


# car method for the position of the car
def car(x, y):
    gameDisplay.blit(carImage, (x, y))


# bot image method
def objects(object_x, object_y, object_width, object_height, color):
    pygame.draw.rect(gameDisplay, color, [object_x, object_y, object_width, object_height])


# game loop
def game_loop():
    # position of car
    x = (display_width * 0.4)
    y = (display_height * 0.75)

    x_left = 0
    x_right = 0

    # obects parameters
    object_start_x = random.randrange(0, display_width)
    object_start_y = -600
    object_speed = 7
    object_height = 100
    object_width = 100

    # Game Logic
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():                            # For closing the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:                        # when a key is pressed down
                if event.key == pygame.K_LEFT:                      # left arrow key
                    x_left = -5
                if event.key == pygame.K_RIGHT:                     # right arrow key
                    x_right = +5

            if event.type == pygame.KEYUP:                          # when the key is released
                if event.key == pygame.K_LEFT:                      # left arrow key
                    x_left = 0
                if event.key == pygame.K_RIGHT:                     # right arrow key
                    x_right = 0

        # change the position of the car
        x += x_left
        x += x_right

        # position the car on the surface
        gameDisplay.fill(white)

        # objects location
        objects(object_start_x, object_start_y, object_width, object_height, black)
        object_start_y += object_speed


        car(x, y)

        if x > (display_width - car_width) or x < 0:                    # if the car goes outside the boundary
            crashed()

        if object_start_y > display_height:                             # object repeats itself
            object_start_y = 0 - object_height
            object_start_x = random.randrange(0, display_width)

        if y < object_start_y+object_height:                            # object crash logic

            if x > object_start_x and x < object_start_x + object_width or x+car_width > object_start_x and x + car_width < object_start_x+object_width:
                crashed()

        pygame.display.update()
        clock.tick(120)


# crashed method
def crashed():
   crashed_message('You have crashed!')


# text objects
def text_objects(message, font):
    text = font.render(message, True, black)
    return text, text.get_rect()


# crashed message
def crashed_message(message):
    large_text = pygame.font.Font('freesansbold.ttf', 75)
    text_surface, text_rectangle = text_objects(message, large_text)
    text_rectangle.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(text_surface, text_rectangle)
    pygame.display.update()
    time.sleep(2)
    game_loop()


game_loop()
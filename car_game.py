import pygame
import random

# setting up the widths and height
width, height = 500, 600
road_width = width//1.3

# creating the window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Car Game')

# creating font
pygame.font.init()
lost_font = pygame.font.SysFont('Comic Sans MS', 75)

# car of the user
user_car_image = pygame.transform.scale(pygame.image.load('car_images/car.png'), (150, 150))
# car of the user
game_car_image = pygame.transform.scale(pygame.image.load('car_images/otherCar.png'), (150, 150))

def show(user_car, game_car):
    # giving a background color
    window.fill((50, 205, 50))

    # the road
    pygame.draw.rect(window, (0, 0, 0), (width//2-road_width//2, 0, road_width, height))
    # line in the middle of the road
    pygame.draw.rect(window, (255, 211, 0), (width//2-4, 0, 8, height))
    # lines in the right and left sides of the road
    pygame.draw.rect(window, (255, 255, 255), (width//2 - road_width//2 + 16, 0, 8, height))
    pygame.draw.rect(window, (255, 255, 255), (width//2 + road_width//2 - 22, 0, 8, height))

    # displying the cars
    window.blit(user_car_image, (user_car.x, user_car.y))
    window.blit(game_car_image, (game_car.x, game_car.y))

    pygame.display.update()

def show_lost():
    # to show that the player has lost
    lost = lost_font.render('You Lost!', 1, (255, 255, 255))
    window.blit(lost, (width//2 - lost.get_width() + 160, height//2 - lost.get_height()))
    pygame.display.update()
    pygame.time.delay(2000)

# mainloop
def main():
    # creating user car and game car objects
    user_car = pygame.Rect(road_width - 120, height - 160, 150, 150)
    game_car = pygame.Rect(road_width - 295, 0, 150, 150)

    # initial speed of the car
    speed = 1
    # initializing millisecond count
    count = 0

    run = True
    while run:
        # increasing the spped of the car per 10 seconds
        count += 1
        if count == 5000:
            speed += 0.1
            count = 0

        for event in pygame.event.get():
            # quitting the game
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                return

            # moving according to the keys pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and user_car.x - 175 > 0:
                    user_car.x -= 175
                if event.key == pygame.K_RIGHT and user_car.x + 175*2 < width:
                    user_car.x += 175
        
        # moving the enemy car
        game_car.y += speed
        if game_car.y >= height:
            game_car.y = 0

            # choosing a random place where the enemy car should appear
            if random.randint(0, 1) == 0:
                game_car.x = road_width - 295
            else:
                game_car.x = road_width - 120

        # if a car has crashed
        if game_car.colliderect(user_car):
            show_lost()
            main()
            return

        # show things onto the screen
        show(user_car, game_car)

main()

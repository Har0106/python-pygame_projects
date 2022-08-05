import pygame

# setting up the window of the game
width, height = 900, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Shooter')

# images used for the game
space = pygame.transform.scale(pygame.image.load('image_and_audio/space.png'), (width, height))
yellow_spaceship = pygame.transform.scale(pygame.image.load('image_and_audio/spaceship_yellow.png'), (125, 65))
red_spaceship = pygame.transform.scale(pygame.image.load('image_and_audio/spaceship_red.png'), (125, 65))

def yellow_movement(yellow, keys_pressed):
    # moving spaceships according to the keys pressed
    if keys_pressed[pygame.K_a]:
        yellow.x -= 3
    if keys_pressed[pygame.K_d]:
        yellow.x += 3
    if keys_pressed[pygame.K_s]:
        yellow.y += 3
    if keys_pressed[pygame.K_w]:
        yellow.y -= 3

def red_movement(red, keys_pressed):
    # moving spaceships according to the keys pressed
    if keys_pressed[pygame.K_LEFT]:
        red.x -= 3
    if keys_pressed[pygame.K_RIGHT]:
        red.x += 3
    if keys_pressed[pygame.K_DOWN]:
        red.y += 3
    if keys_pressed[pygame.K_UP]:
        red.y -= 3

def show(red, yellow):
    # put images onto the screen
    window.blit(space, (0, 0))
    window.blit(pygame.transform.rotate(yellow_spaceship, 90), (yellow.x, yellow.y))
    window.blit(pygame.transform.rotate(red_spaceship, 270), (red.x, red.y))

    pygame.display.update()

# creating the mainloop of the game
def main():
    clock = pygame.time.Clock()

    # set initial position of the spaceships
    yellow = pygame.Rect(90, 190, 125, 65)
    red = pygame.Rect(750, 190, 125, 65)

    run = True
    while run:
        # setting the spped of the whileloop
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                return
        
        # get pressed keys
        keys_pressed = pygame.key.get_pressed()

        # moving spaceships
        yellow_movement(yellow, keys_pressed)
        red_movement(red, keys_pressed)

        show(red, yellow)

main()
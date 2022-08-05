import pygame

# setting up the window of the game
width, height = 900, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Shooter')

# images used for the game
space = pygame.transform.scale(pygame.image.load('image_and_audio/space.png'), (width, height))
yellow_spaceship = pygame.transform.scale(pygame.image.load('image_and_audio/spaceship_yellow.png'), (80, 45))
red_spaceship = pygame.transform.scale(pygame.image.load('image_and_audio/spaceship_red.png'), (80, 45))

border = pygame.Rect(width//2 - 4, 0, 8, height)

yellow_event = pygame.USEREVENT + 1
red_event = pygame.USEREVENT + 2

def yellow_movement(yellow, keys_pressed):
    # moving spaceships according to the keys pressed
    if keys_pressed[pygame.K_a] and yellow.x - 3 > 0:
        yellow.x -= 3
    if keys_pressed[pygame.K_d] and yellow.x + 3 + yellow.width < border.x + 60:
        yellow.x += 3
    if keys_pressed[pygame.K_s] and yellow.y + 3 + yellow.height < height - 57:
        yellow.y += 3
    if keys_pressed[pygame.K_w] and yellow.y - 3 > 0:
        yellow.y -= 3

def red_movement(red, keys_pressed):
    # moving spaceships according to the keys pressed
    if keys_pressed[pygame.K_LEFT] and red.x - 3 > border.x + border.width:
        red.x -= 3
    if keys_pressed[pygame.K_RIGHT] and red.x + 3 + red.width < width + 60:
        red.x += 3
    if keys_pressed[pygame.K_DOWN] and red.y + 3 + red.height < height - 57:
        red.y += 3
    if keys_pressed[pygame.K_UP] and red.y - 3 > 0:
        red.y -= 3

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += 7
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_event))
            yellow_bullets.remove(bullet)
        elif bullet.x > width:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= 7
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_event))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def show(red, yellow, red_bullets, yellow_bullets):
    # put images onto the screen
    window.blit(space, (0, 0))
    pygame.draw.rect(window, (0, 0, 0), border)
    window.blit(pygame.transform.rotate(yellow_spaceship, 90), (yellow.x, yellow.y))
    window.blit(pygame.transform.rotate(red_spaceship, 270), (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(window, (255, 0, 0), bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(window, (255, 225, 0), bullet)

    pygame.display.update()

# creating the mainloop of the game
def main():
    clock = pygame.time.Clock()

    # set initial position of the spaceships
    yellow = pygame.Rect(90, 190, 125, 65)
    red = pygame.Rect(750, 190, 125, 65)

    yellow_bullets = []
    red_bullets = []

    run = True
    while run:
        # setting the spped of the whileloop
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < 5:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < 5:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
        
        # get pressed keys
        keys_pressed = pygame.key.get_pressed()

        # moving spaceships
        yellow_movement(yellow, keys_pressed)
        red_movement(red, keys_pressed)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        show(red, yellow, red_bullets, yellow_bullets)

main()
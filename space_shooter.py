import pygame

# creating fonts
pygame.font.init()
health_font = pygame.font.SysFont('Comic Sans MS', 25)
winner_font = pygame.font.SysFont('Comic Sans MS', 100)

# setting up the window of the game
width, height = 900, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Shooter')

# images used for the game
space = pygame.transform.scale(pygame.image.load('image_and_audio/space.png'), (width, height))
yellow_spaceship = pygame.transform.scale(pygame.image.load('image_and_audio/spaceship_yellow.png'), (80, 45))
red_spaceship = pygame.transform.scale(pygame.image.load('image_and_audio/spaceship_red.png'), (80, 45))

# the border between two spaceships
border = pygame.Rect(width//2 - 4, 0, 8, height)

# definig events
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
    # moving yellow bullets
    for bullet in yellow_bullets:
        bullet.x += 7
        # setting the event if a bullet has hit the spaceship
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_event))
            yellow_bullets.remove(bullet)
        # removing bullet from list if it has passesd the screen
        elif bullet.x > width:
            yellow_bullets.remove(bullet)

    # moving red bullets
    for bullet in red_bullets:
        bullet.x -= 7
        # setting the event if a bullet has hit the spaceship
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_event))
            red_bullets.remove(bullet)
        # removing bullet from list if it has passesd the screen
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def show(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    # background of the game
    window.blit(space, (0, 0))

    # border between two spaceships
    pygame.draw.rect(window, (0, 0, 0), border)

    # text to show the remainig health
    yellow_health_text = health_font.render(f'Health: {yellow_health}', 1, (255, 255, 255))
    red_health_text = health_font.render(f'Health: {red_health}', 1, (255, 255, 255))
    window.blit(yellow_health_text, (10, 10))
    window.blit(red_health_text, (width - yellow_health_text.get_width() - 10, 10))

    # spaceships
    window.blit(pygame.transform.rotate(yellow_spaceship, 90), (yellow.x, yellow.y))
    window.blit(pygame.transform.rotate(red_spaceship, 270), (red.x, red.y))

    # bullets
    for bullet in red_bullets:
        pygame.draw.rect(window, (255, 0, 0), bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(window, (255, 225, 0), bullet)

    pygame.display.update()

def show_winner(text):
    # text to show the winner
    winner_text = winner_font.render(text, 1, (255, 255, 255))
    window.blit(winner_text, (width//2 - winner_text.get_width() + 260, height//2 - winner_text.get_height() + 50))
    pygame.display.update()
    pygame.time.delay(2000)

# creating the mainloop of the game
def main():
    clock = pygame.time.Clock()

    # set initial position of the spaceships
    yellow = pygame.Rect(90, 190, 125, 65)
    red = pygame.Rect(750, 190, 125, 65)

    yellow_bullets = []
    red_bullets = []

    # initializing the health of spaceships
    yellow_health = 10
    red_health = 10

    text = ''

    run = True
    while run:
        # setting the speed of the whileloop
        clock.tick(60)
        
        for event in pygame.event.get():
            # quit the game if close is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                return

            # to shoot bullets
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < 5:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < 5:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)

            # to decrease health if a spaceship is hit
            if event.type == yellow_event:
                yellow_health -= 1
            if event.type == red_event:
                red_health -= 1

        # to determine the winner
        if yellow_health <= 0:
            text = 'Red Won!'
        elif red_health <= 0:
            text = 'Yellow Won!'
        
        # get pressed keys
        keys_pressed = pygame.key.get_pressed()

        # moving spaceships
        yellow_movement(yellow, keys_pressed)
        red_movement(red, keys_pressed)

        # moving and setting the event of bullets
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        # displaying images, rectangle and font in the screen
        show(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

        # dispaying the winner and restarting the game
        if text:
            show_winner(text)
            main()
            return

main()
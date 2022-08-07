import pygame

length = 600
rows = 20

# creating the main window
window = pygame.display.set_mode((length, length))
pygame.display.set_caption('Snake Game')

# moving the snake
def move(keys, snake):
    if keys[pygame.K_LEFT]:
        snake.x = snake.x - 30
    if keys[pygame.K_RIGHT]:
        snake.x = snake.x + 30
    if keys[pygame.K_UP]:
        snake.y = snake.y - 30
    if keys[pygame.K_DOWN]:
        snake.y = snake.y + 30

def show(snake):
    # setting the background
    window.fill((0, 0, 0))

    # drwing the grid
    pos = 0
    for i in range(rows):
        pos += length // rows
        pygame.draw.line(window, (152, 152, 152), (pos, 0), (pos, length))
        pygame.draw.line(window, (152, 152, 152), (0, pos), (length, pos))

    # creating the head of the snake
    pygame.draw.rect(window, (5, 71, 42), (snake.x, snake.y, 30, 30))

    pygame.display.update()

def main():
    # creating a clock object
    clock = pygame.time.Clock()

    snake = pygame.Rect(300, 300, 30, 30)

    # mainloop
    run = True
    while run:
        clock.tick(10)

        # quitting pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                return

        keys = pygame.key.get_pressed()

        move(keys, snake)
        show(snake)
    
main()
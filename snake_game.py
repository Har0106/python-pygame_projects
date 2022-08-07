import pygame

length = 600
rows = 20

# creating the main window
window = pygame.display.set_mode((length, length))
pygame.display.set_caption('Snake Game')

def show():
    # setting the background
    window.fill((0, 0, 0))

    # drwing the grid
    pos = 0
    for i in range(rows):
        pos += 30
        pygame.draw.line(window, (152, 152, 152), (pos, 0), (pos, length))
        pygame.draw.line(window, (152, 152, 152), (0, pos), (length, pos))

    pygame.display.update()

def main():
    # creating a clock object
    clock = pygame.time.Clock()

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

        show()
    
main()
import pygame

# setting up the window of the game
width, height = 900, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Shooter')

# creating the mainloop of the game
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

main()
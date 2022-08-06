import pygame

width, height = 500, 600
road_width = width//1.3

# creating the window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Car Game')

# giving a background color
window.fill((50, 205, 50))

# the road
pygame.draw.rect(window, (0, 0, 0), (width//2-road_width//2, 0, road_width, height))
# line in the middle of the road
pygame.draw.rect(window, (255, 211, 0), (width//2-4, 0, 8, height))
# lines in the right and left sides of the road
pygame.draw.rect(window, (255, 255, 255), (width//2 - road_width//2 + 16, 0, 8, height))
pygame.draw.rect(window, (255, 255, 255), (width//2 + road_width//2 - 22, 0, 8, height))
pygame.display.update()

# mainloop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
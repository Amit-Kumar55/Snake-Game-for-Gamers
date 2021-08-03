import pygame
pygame.init()
# creating window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My first game")
# Game specific variable
exit_game = False
game_over = False

# creating game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()

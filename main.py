import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

HEIGHT = 900
WIDTH = 500

screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Space shooter")

SPACESHIP_HEIGHT = 55
SPACESHIP_WIDTH = 40

BG = pygame.image.load('Assets/space.png')
RED_SPACESHIP_IMG = pygame.image.load('Assets/spaceship_red.png')
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMG, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH))
YELLOW_SPACESHIP_IMG = pygame.image.load('Assets/spaceship_yellow.png')
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMG, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH))


def draw_screen():

    screen.blit(BG, (0, 0))
    screen.blit(RED_SPACESHIP, (100, 250))
    screen.blit(YELLOW_SPACESHIP, (700, 250))
    pygame.display.update()


def main():

    run = True
    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_screen()

    pygame.quit()

if __name__ == "__main__":
    main()
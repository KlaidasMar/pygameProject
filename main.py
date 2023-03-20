import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

HEIGHT = 900
WIDTH = 500

screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Space shooter")

BG = pygame.image.load('Assets/space.png')
WHITE = (255, 255, 255)

def draw_screen():
    screen.fill(WHITE)
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
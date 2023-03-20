import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

VEL = 5

HEIGHT = 900
WIDTH = 500

screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Space shooter")

SPACESHIP_HEIGHT = 55
SPACESHIP_WIDTH = 40

BG = pygame.image.load('Assets/space.png')
RED_SPACESHIP_IMG = pygame.image.load('Assets/spaceship_red.png')
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH)),
                                        90)
YELLOW_SPACESHIP_IMG = pygame.image.load('Assets/spaceship_yellow.png')
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMG, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH)), 270)


def draw_screen(red, yellow):
    screen.blit(BG, (0, 0))
    screen.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    screen.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d]:
        yellow.x += VEL
    if keys_pressed[pygame.K_w]:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s]:
        yellow.y += VEL


def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:
        red.x += VEL
    if keys_pressed[pygame.K_UP]:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN]:
        red.y += VEL


def main():
    red = pygame.rect.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.rect.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    run = True
    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)

        draw_screen(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()

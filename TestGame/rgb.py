import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("RGB Demo")

    clock = pygame.time.Clock()
    running = True

    background_color = WHITE

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    background_color = RED
                elif event.key == pygame.K_g:
                    background_color = GREEN
                elif event.key == pygame.K_b:
                    background_color = BLUE
            elif event.type == pygame.KEYUP:
                background_color = WHITE
                

        screen.fill(background_color)

        pygame.display.flip()
        
        clock.tick(FPS)

    pygame.quit()



if __name__ == "__main__":
    main()
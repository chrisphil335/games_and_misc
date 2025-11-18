import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pygame Boilerplate")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        
        clock.tick(FPS)

    pygame.quit()



if __name__ == "__main__":
    main()
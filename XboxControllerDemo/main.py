import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Xbox Controller Demo")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()



if __name__ == "__main__":
    main()
import pygame


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        screen.fill("green")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

        pygame.draw.circle(screen, "blue", player_position, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_position.y -= 300 * dt
        if keys[pygame.K_a]:
            player_position.x -= 300 * dt
        if keys[pygame.K_s]:
            player_position.y += 300 * dt
        if keys[pygame.K_d]:
            player_position.x += 300 * dt

        pygame.display.flip()

        dt = clock.tick(60) / 1000
    pygame.quit()


if __name__ == "__main__":
    main()
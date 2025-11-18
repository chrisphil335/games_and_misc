import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def main():
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Detected joystick: {joystick.get_name()}")
    else:
        print("No joystick detected")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Xbox Controller Demo")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    print("A button pressed")
                elif event.button == 1:
                    print("B button pressed")
                elif event.button == 2:
                    print("X button pressed")
                elif event.button == 3:
                    print("Y button pressed")
                elif event.button == 4:
                    print("Left bumper pressed")
                elif event.button == 5:
                    print("Right bumper pressed")
                

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
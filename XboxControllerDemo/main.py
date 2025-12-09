import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60


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
                elif event.button == 6:
                    print("Back button pressed")
                elif event.button == 7:
                    print("Start button pressed")
                elif event.button == 8:
                    print("Left stick in pressed")
                elif event.button == 9:
                    print("Right stick in pressed")
                elif event.button == 10:
                    print("Guide button pressed")
                
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
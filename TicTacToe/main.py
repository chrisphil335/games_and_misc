import pygame

LINE_WIDTH = 5
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
CELL_WIDTH = SCREEN_WIDTH / 3
CELL_HEIGHT = SCREEN_HEIGHT / 3
BOARD = [
    ['', '', ''], 
    ['', '', ''], 
    ['', '', '']
]
PLAYER_1 = "X"
PLAYER_2 = "O"



def draw_board(screen):
    # horizontals
    pygame.draw.line(screen, "yellow", pygame.Vector2(0, SCREEN_HEIGHT / 3), pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT / 3), width = LINE_WIDTH)
    pygame.draw.line(screen, "yellow", pygame.Vector2(0, SCREEN_HEIGHT / 3 * 2), pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT / 3 * 2), width = LINE_WIDTH)
    # verticals
    pygame.draw.line(screen, "yellow", pygame.Vector2(SCREEN_WIDTH / 3, 0), pygame.Vector2(SCREEN_WIDTH / 3, SCREEN_HEIGHT), width = LINE_WIDTH)
    pygame.draw.line(screen, "yellow", pygame.Vector2(SCREEN_WIDTH / 3 * 2, 0), pygame.Vector2(SCREEN_WIDTH / 3 * 2, SCREEN_HEIGHT), width = LINE_WIDTH)


def draw_x(screen, start_x, start_y, x_width, x_height):
    pygame.draw.line(screen, "red", pygame.Vector2(start_x, start_y), pygame.Vector2(start_x + x_width, start_y + x_height), width = LINE_WIDTH)
    pygame.draw.line(screen, "red", pygame.Vector2(start_x + x_width, start_y), pygame.Vector2(start_x, start_y + x_height), width = LINE_WIDTH)


def draw_o(screen, start_x, start_y, x_width, x_height):
    pygame.draw.line(screen, "red", pygame.Vector2(start_x, start_y), pygame.Vector2(start_x + x_width, start_y + x_height), width = LINE_WIDTH)


def winner_check(current_player):
    if BOARD[0][0] == BOARD[0][1] == BOARD[0][2] != "":
        print(current_player)
        return True


def reset_game(screen):
    screen.fill("green")


def change_current_player(current_player):
    if current_player == PLAYER_1:
        return PLAYER_2
    elif current_player == PLAYER_2:
        return PLAYER_1


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    reset_game(screen)
    draw_board(screen)
    current_player = PLAYER_1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                column = int(event.pos[0] // CELL_WIDTH)
                row = int(event.pos[1] // CELL_HEIGHT)
                if current_player == "X":
                    draw_x(screen, column * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
                    BOARD[row][column] = "X"
                elif current_player == "O":
                    draw_o(screen, column * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
                    BOARD[row][column] = "O"
            if winner_check(current_player):
                running = False
            current_player = change_current_player(current_player)
                

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            reset_game(screen)

        

        pygame.display.flip()

        dt = clock.tick(60) / 1000
    pygame.quit()


if __name__ == "__main__":
    main()
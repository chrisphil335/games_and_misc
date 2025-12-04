import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60
BOARD = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
CELL_WIDTH = SCREEN_WIDTH / 3
CELL_HEIGHT = SCREEN_HEIGHT / 3
LINE_WIDTH = 5
BACKGROUND_COLOR = "green"
GRID_COLOR = "yellow"
X_COLOR = "blue"
O_COLOR = "red"


def draw_grid(screen):
    # horizontals
    pygame.draw.line(screen, GRID_COLOR, pygame.Vector2(0, CELL_HEIGHT), pygame.Vector2(SCREEN_WIDTH, CELL_HEIGHT), width = LINE_WIDTH)
    pygame.draw.line(screen, GRID_COLOR, pygame.Vector2(0, CELL_HEIGHT * 2), pygame.Vector2(SCREEN_WIDTH, CELL_HEIGHT * 2), width = LINE_WIDTH)
    # verticals
    pygame.draw.line(screen, GRID_COLOR, pygame.Vector2(CELL_WIDTH, 0), pygame.Vector2(CELL_WIDTH, SCREEN_HEIGHT), width = LINE_WIDTH)
    pygame.draw.line(screen, GRID_COLOR, pygame.Vector2(CELL_WIDTH * 2, 0), pygame.Vector2(CELL_WIDTH * 2, SCREEN_HEIGHT), width = LINE_WIDTH)


def switch_player(current_player):
    if current_player == "X":
        return "O"
    elif current_player == "O":
        return "X"
    

def draw_x(screen, x, y, width, height):
    pygame.draw.line(screen, X_COLOR, pygame.Vector2(x, y), pygame.Vector2(x + width, y + height), width = LINE_WIDTH)
    pygame.draw.line(screen, X_COLOR, pygame.Vector2(x + width, y), pygame.Vector2(x, y + height), width = LINE_WIDTH)


def draw_o(screen, x, y, width, height):
    pygame.draw.circle(screen, O_COLOR, pygame.Vector2(x + width / 2, y + height / 2), min(width, height) / 3, width = LINE_WIDTH)


def draw_pieces(screen):
    for row in range(len(BOARD)):
        for column in range(len(BOARD[0])):
            cell = BOARD[row][column]
            start_x = column * CELL_WIDTH
            start_y = row * CELL_HEIGHT
            if cell == "X":
                draw_x(screen, start_x, start_y, CELL_WIDTH, CELL_HEIGHT)
            elif cell == "O":
                draw_o(screen, start_x, start_y, CELL_WIDTH, CELL_HEIGHT)


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    for column in range(len(board[0])):
        if board[0][column] == board[1][column] == board[2][column] != "":
            return board[0][column]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None


def is_draw(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True


def reset_board():
    for row in BOARD:
        for column in range(len(row)):
            row[column] = ""


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tictactoe")

    clock = pygame.time.Clock()
    running = True
    game_over = False

    current_player = "X"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                column = int(event.pos[0] // CELL_WIDTH)
                row = int(event.pos[1] // CELL_HEIGHT)
                print(f"({row}, {column})")
                if BOARD[row][column] == "":
                    BOARD[row][column] = current_player
                    winner = check_winner(BOARD)
                    if winner:
                        print(f"{current_player} wins!")
                        game_over = True
                    elif is_draw(BOARD):
                        print("Draw!")
                        game_over = True
                    else:
                        current_player = switch_player(current_player)
                    print(BOARD)
                else:
                    print("occupied")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_board()
                    current_player = "X"
                    game_over = False

        screen.fill(BACKGROUND_COLOR)
        draw_grid(screen)
        draw_pieces(screen)
        pygame.display.flip() 
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
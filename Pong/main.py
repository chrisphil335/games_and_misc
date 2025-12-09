import pygame
import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0) # Black
WHITE = (255, 255, 255)
BALL_SIZE = 20
PADDLE_HEIGHT = SCREEN_HEIGHT // 5
PADDLE_WIDTH = PADDLE_HEIGHT // 15
PADDLE_SPEED = 5
PADDLE_OFFSET = PADDLE_WIDTH


def draw(screen, ball, player1, player2):
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, WHITE, ball, border_radius = BALL_SIZE // 2)
    pygame.draw.rect(screen, WHITE, player1, border_radius = PADDLE_WIDTH // 2)
    pygame.draw.rect(screen, WHITE, player2, border_radius = PADDLE_WIDTH // 2)
    pygame.display.flip()


def reset_ball(ball_rect):
    ball_rect.x = (SCREEN_WIDTH - BALL_SIZE) // 2
    ball_rect.y = (SCREEN_HEIGHT - BALL_SIZE) // 2
    
    new_ball_speed_x = random.choice([-4, -3, 3, 4])
    new_ball_speed_y = random.choice([-3, -2, 2, 3])

    return new_ball_speed_x, new_ball_speed_y


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")

    clock = pygame.time.Clock()
    running = True

    ball_x = (SCREEN_WIDTH - BALL_SIZE) // 2
    ball_y = (SCREEN_HEIGHT - BALL_SIZE) // 2
    ball_rect = pygame.Rect(ball_x, ball_y, BALL_SIZE, BALL_SIZE)
    ball_speed_x, ball_speed_y = reset_ball(ball_rect)

    player1_x = PADDLE_OFFSET
    player1_y = (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2
    player1_rect = pygame.Rect(player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    player1_score = 0

    player2_x = SCREEN_WIDTH - (PADDLE_OFFSET + PADDLE_WIDTH)
    player2_y = (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2
    player2_rect = pygame.Rect(player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    player2_score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            player1_rect.y = max(0, player1_rect.y - PADDLE_SPEED)
        if keys[pygame.K_s]:
            player1_rect.y = min(player1_rect.y + PADDLE_SPEED, SCREEN_HEIGHT - PADDLE_HEIGHT)
        if keys[pygame.K_UP]:
            player2_rect.y = max(0, player2_rect.y - PADDLE_SPEED)
        if keys[pygame.K_DOWN]:
            player2_rect.y = min(player2_rect.y + PADDLE_SPEED, SCREEN_HEIGHT - PADDLE_HEIGHT)

        ball_rect.x += ball_speed_x
        ball_rect.y += ball_speed_y

        if ball_rect.y <= 0 or ball_rect.y >= SCREEN_HEIGHT - BALL_SIZE:
            ball_speed_y *= -1

        if player1_rect.colliderect(ball_rect) and ball_speed_x < 0:
            ball_speed_x *= -1
            ball_rect.x += ball_speed_x
        elif player2_rect.colliderect(ball_rect) and ball_speed_x > 0:
            ball_speed_x *= -1
            ball_rect.x += ball_speed_x

        if ball_rect.x <= 0:
            player2_score += 1
            print(f"{player1_score}, {player2_score}")
            ball_speed_x, ball_speed_y = reset_ball(ball_rect)
        elif ball_rect.x >= SCREEN_WIDTH:
            player1_score += 1
            print(f"{player1_score}, {player2_score}")
            ball_speed_x, ball_speed_y = reset_ball(ball_rect)

        draw(screen, ball_rect, player1_rect, player2_rect)

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
import pygame

from classes_sn import Snake, Food, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, CELL_SIZE

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

SCORE = 0

snake = Snake()
food = Food()
running = True
while running:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    if snake.alive:
        snake.move()
        if snake.memory_move(food.position):
            food.spawn()
            SCORE += 1
    else:
        pygame.display.set_caption("You lose")
        game_over_text = font.render("GAME OVER", True, BLACK)
        screen.blit(game_over_text, (320, 280))
    snake.draw(screen)
    food.draw(screen)
    score_text = font.render(f"Score - {SCORE}", True, BLACK)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
pygame.quit()
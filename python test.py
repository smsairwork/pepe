

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
ENEMY_WIDTH, ENEMY_HEIGHT = 50, 50
BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (0, 255, 0)
ENEMY_COLOR = (255, 0, 0)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aviator Crash Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player
player_x = WIDTH // 2 - PLAYER_WIDTH // 2
player_y = HEIGHT - PLAYER_HEIGHT - 20
player_speed = 5

# Enemies
enemies = []
enemy_speed = 3

# Game variables
score = 0

# Fonts
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_WIDTH:
        player_x += player_speed

    # Spawn enemies
    if random.randint(1, 100) < 5:  # Adjust the probability as needed
        enemy_x = random.randint(0, WIDTH - ENEMY_WIDTH)
        enemy_y = 0
        enemies.append([enemy_x, enemy_y])

    # Move enemies
    for enemy in enemies:
        enemy[1] += enemy_speed

    # Check for collisions
    for enemy in enemies:
        if (
            player_x < enemy[0] + ENEMY_WIDTH
            and player_x + PLAYER_WIDTH > enemy[0]
            and player_y < enemy[1] + ENEMY_HEIGHT
            and player_y + PLAYER_HEIGHT > enemy[1]
        ):
            running = False

    # Remove off-screen enemies
    enemies = [enemy for enemy in enemies if enemy[1] < HEIGHT]

    # Update the display
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))
    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, (enemy[0], enemy[1], ENEMY_WIDTH, ENEMY_HEIGHT))

    # Update score
    score += 1
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Game over screen
game_over_text = font.render("Game Over", True, (255, 255, 255))
screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 30))
final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
screen.blit(final_score_text, (WIDTH // 2 - 100, HEIGHT // 2 + 20))
pygame.display.flip()

# Wait for a few seconds before closing the game
pygame.time.delay(2000)

# Quit Pygame
pygame.quit()

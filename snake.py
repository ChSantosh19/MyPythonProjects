import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# Font
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

class SnakeGame:
    def __init__(self):
        self.state = "menu"
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]  # List of (x, y) coordinates
        self.direction = (1, 0)  # Initial direction: right
        self.food = self.spawn_food()
        self.score = 0
        self.speed = 10  # Updates per second

    def spawn_food(self):
        while True:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food not in self.snake:
                return food

    def update(self):
        if self.state == "playing":
            # Move snake
            head_x, head_y = self.snake[0]
            dx, dy = self.direction
            new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)

            # Check collision with self
            if new_head in self.snake:
                self.state = "game_over"
                return

            # Add new head
            self.snake.insert(0, new_head)

            # Check food collision
            if new_head == self.food:
                self.score += 1
                self.food = self.spawn_food()
                self.speed += 1  # Increase speed slightly with each food
            else:
                # Remove tail if no food eaten
                self.snake.pop()

    def change_direction(self, new_direction):
        # Prevent reversing direction
        if (new_direction[0] != -self.direction[0] or new_direction[1] != -self.direction[1]):
            self.direction = new_direction

    def draw(self):
        screen.fill(BLACK)
        
        if self.state == "menu":
            title = font.render("Snake", True, GREEN)
            start_text = small_font.render("Press SPACE to start", True, WHITE)
            screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//4))
            screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT//2))
        
        elif self.state in ["playing", "game_over"]:
            # Draw snake
            for segment in self.snake:
                pygame.draw.rect(screen, GREEN, 
                               (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, 
                                GRID_SIZE - 1, GRID_SIZE - 1))
            
            # Draw food
            pygame.draw.rect(screen, RED, 
                           (self.food[0] * GRID_SIZE, self.food[1] * GRID_SIZE, 
                            GRID_SIZE - 1, GRID_SIZE - 1))
            
            # Draw score
            score_text = small_font.render(f"Score: {self.score}", True, WHITE)
            screen.blit(score_text, (10, 10))
            
            if self.state == "game_over":
                game_over = font.render("Game Over", True, WHITE)
                restart_text = small_font.render("Press R to restart", True, WHITE)
                screen.blit(game_over, (WIDTH//2 - game_over.get_width()//2, HEIGHT//3))
                screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2))

# Game loop
game = SnakeGame()
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.state == "menu":
                game.state = "playing"
            elif event.key == pygame.K_r and game.state == "game_over":
                game = SnakeGame()
            elif game.state == "playing":
                if event.key == pygame.K_UP:
                    game.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    game.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    game.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    game.change_direction((1, 0))

    game.update()
    game.draw()
    pygame.display.flip()
    clock.tick(game.speed if game.state == "playing" else 60)

pygame.quit()
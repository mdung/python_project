import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Main Menu")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, x, y):
    """Draw text on the screen."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main_menu():
    while True:
        screen.fill(WHITE)

        # Draw menu options
        draw_text("Main Menu", font, BLACK, width // 2, height // 4)
        draw_text("1. Start Game", font, BLACK, width // 2, height // 2)
        draw_text("2. Settings", font, BLACK, width // 2, height // 2 + 50)
        draw_text("3. Instructions", font, BLACK, width // 2, height // 2 + 100)
        draw_text("4. Quit", font, BLACK, width // 2, height // 2 + 150)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("Starting game...")
                    # Add your game start logic here
                elif event.key == pygame.K_2:
                    print("Accessing settings...")
                    # Add your settings logic here
                elif event.key == pygame.K_3:
                    print("Viewing instructions...")
                    # Add your instructions logic here
                elif event.key == pygame.K_4:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main_menu()

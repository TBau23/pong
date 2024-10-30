def draw_text(screen, text, size, color, x, y):
    """Helper function to display text on the screen."""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def start_screen(screen):
    """Displays the start screen and waits for player input."""
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN: 
                waiting = False

        # Fill the screen with black and display the start message
        screen.fill("black")
        draw_text(screen, "Press any key to start", 50, (255, 255, 255), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        pygame.display.flip()

def game_over_screen(screen):
    """Displays the game over screen and waits for player input."""
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return event.key  

        screen.fill("black")
        draw_text(screen, "Game Over!", 80, (255, 0, 0), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50)
        draw_text(screen, "Press R to Restart or Q to Quit", 50, (255, 255, 255), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50)
        pygame.display.flip()
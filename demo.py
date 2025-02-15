import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_SPEED = 5  # Adjust this value to change scrolling speed

# Colors
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scrolling Background")

# Load background image
background_image = pygame.image.load("graphics/ground.png")  # Replace with your image path

# Get image width and height
bg_width = background_image.get_width()
bg_height = background_image.get_height()

# Initial position of the background
bg_x = 0

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update background position
    bg_x -= BG_SPEED

    # Reset the background position if it goes off-screen
    if bg_x <= -bg_width:
        bg_x = 0

    # Draw background
    screen.fill(WHITE)  # Fill screen with a background color (optional)
    screen.blit(background_image, (bg_x, 0))
    screen.blit(background_image, (bg_x + bg_width, 0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

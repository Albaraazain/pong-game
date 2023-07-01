import pygame
from pygame.locals import *

# Initializing Pygame
pygame.init()

# Setting up the game window dimensions
window_width, window_height = 800, 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong")  # name of the game

# Defining the color white for later use
WHITE = (255, 255, 255)

# paddles dimensions and initial positions
paddle_width, paddle_height = 10, 60
paddle_speed = 5
left_paddle_pos = pygame.Rect(50, window_height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle_pos = pygame.Rect(window_width - 50 - paddle_width, window_height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Configuring the balls dimensions, position, and speed
ball_radius = 10
# Rect for rectangle. (left, top, width, and height)
# Height, width is the radius
ball_pos = pygame.Rect(window_width // 2 - ball_radius // 2, window_height // 2 - ball_radius // 2, ball_radius, ball_radius)
ball_speed_x = 3
ball_speed_y = 3

# Control the timing and frame rate, meaning we can regulate the speed at which the game updates and redraws the screen
clock = pygame.time.Clock()  # Setting up the clock for timing control

running = True  # The loop for running the game
while running:
    # pygame.event.get() function retrieves all the events that have occurred since the last time it was called like...
    # ...user input events (such as keyboard or mouse events), window-related events (like closing the window),
    # and various other system events.
    for event in pygame.event.get():
        # check the event type if its QUIT then we quit the game
        if event.type == QUIT:   # Checking if we should quit the game
            running = False

    # pygame.key.get_pressed() returns a list of boolean values representing the state of all keys on the keyboard
    keys = pygame.key.get_pressed()  # Checking which keys are pressed

    # Moving the paddles based on key inputs
    # keys[K_w] to check if the 'W' key is currently being pressed
    # left_paddle_pos.top > 0, to check if the top edge of the paddle is not at the top edge of the screen
    # (basically to check if there's space for the paddle to go up)
    if keys[K_w] and left_paddle_pos.top > 0:
        # The move_ip() method of the pygame.Rect object updates the position of the rectangle by modifying its top
        # and left attributes (x,y). In this case, the paddle is moved upwards by subtracting paddle_speed from its
        # current y-coordinate.
        left_paddle_pos.move_ip(0, -paddle_speed)
    if keys[K_s] and left_paddle_pos.bottom < window_height:
        left_paddle_pos.move_ip(0, paddle_speed)
    if keys[K_UP] and right_paddle_pos.top > 0:
        right_paddle_pos.move_ip(0, -paddle_speed)
    if keys[K_DOWN] and right_paddle_pos.bottom < window_height:
        right_paddle_pos.move_ip(0, paddle_speed)

    ball_pos.move_ip(ball_speed_x, ball_speed_y)  # Moving the ball based on its speed

    # Checking for collisions with the walls and changing ball direction if needed
    if ball_pos.left <= 0 or ball_pos.right >= window_width:    # The X
        ball_speed_x *= -1
    if ball_pos.top <= 0 or ball_pos.bottom >= window_height:   # The Y
        ball_speed_y *= -1

    # Checking for collisions with the paddles and bouncing off accordingly checks if the ball collides with the left
    # The colliderect() method of pygame.Rect objects returns True if two rectangles overlap or intersect.
    if ball_pos.colliderect(left_paddle_pos) or ball_pos.colliderect(right_paddle_pos):
        ball_speed_x *= -1

    # DRAWING PHASE
    window.fill((0, 0, 0))  # Clearing the window with a black color

    # Drawing the paddles and the ball on the window
    pygame.draw.rect(window, WHITE, left_paddle_pos)
    pygame.draw.rect(window, WHITE, right_paddle_pos)
    pygame.draw.ellipse(window, WHITE, ball_pos)

    pygame.display.update()  # Updating the display
    clock.tick(60)  # Controlling the frame rate to 60 frames per second

# Exiting the game
pygame.quit()



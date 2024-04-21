import pygame
import random
import sys

pygame.init()

# Setting up game window
window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255,255,255)
black = (0,0,0,0)
red = (255,0,0)
grey = (200, 200, 200)

# Function to display a popup
def show_popup(message, score):
    popup_width = 300
    popup_height = 150
    
    # Create a surface for the popup window
    popup_surface = pygame.Surface((popup_width, popup_height))
    popup_surface.fill(white)
    
    # Draw a border around the popup
    pygame.draw.rect(popup_surface, black, (0, 0, popup_width, popup_height), 2)
    
    # Render the message text
    font = pygame.font.Font(None, 25)
    # text = font.render(message, True, black)
    text = font_style.render(message, True, black)
    score_text = font_style.render(f"Score: {score}", True, black)
    window.blit(score_text,[10,10])
    
    # Center the text on the popup surface
    text_rect = text.get_rect(center=(popup_width // 2, (popup_height // 2 ) - 15))
    score_text_rect = score_text.get_rect(center=(popup_width // 2, (popup_height // 2) + 15))
    popup_surface.blit(text, text_rect)
    popup_surface.blit(score_text, score_text_rect)
    
    # Position the popup in the center of the screen
    popup_x = (window_width - popup_width) // 2
    popup_y = (window_height - popup_height) // 2
    
    # Main loop for the popup
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Draw the popup on the main screen
        window.blit(popup_surface, (popup_x, popup_y))
        pygame.display.flip()




# Setting up game variables

speed = 10
score = 0
# Setting up snake
snake_body = []
snake_lenght = 1

x1 = window_width/2
y1 = window_height/2

x1_change = 0
y1_change = 0

food_x = round(random.randrange(0,window_width-10)/10) * 10.0
food_y = round(random.randrange(0,window_height-10)/10) * 10.0

clock = pygame.time.Clock()


# Game loop
game_over = False

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    
    # Check for arrow keys pressed
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        x1_change = -10
        y1_change = 0

      elif event.key == pygame.K_RIGHT:
        x1_change = 10
        y1_change = 0
      
      elif event.key == pygame.K_UP:
        x1_change = 0
        y1_change = -10
      
      elif event.key == pygame.K_DOWN:
        x1_change = 0
        y1_change = 10

  # Update game
  x1 = x1 + x1_change
  y1 = y1 + y1_change

  # Boundary Conditions
  if x1 >= window_width or x1<0 or y1>=window_height or y1<0:
    # Game over
    show_popup("Game Over", score)
    game_over = True

  # Fill background
  window.fill(black)

  # Snake head
  snake_head = []
  snake_head.append(x1)
  snake_head.append(y1)

  snake_body.append(snake_head)

  # Manage snakes lenght
  if len(snake_body)>snake_lenght:
    del snake_body[0]

  # If snake eats itself 
  for segment in snake_body[:-1]:
    if segment == snake_head:
      # Game over
      show_popup("Game Over", score)
      game_over = True
  
  # Display Score
  font_style = pygame.font.SysFont(None,25)
  score_text = font_style.render("Score: " + str(score),True,white)
  window.blit(score_text,[10,10])

  # Check for food collision
  if x1 == food_x and y1 == food_y:
    # Generate new food
    food_x = round(random.randrange(0,window_width-10)/10) * 10.0
    food_y = round(random.randrange(0,window_height-10)/10) * 10.0
    # Increase snake length
    snake_lenght += 1
    # Increase score
    score += 1
    # Increase game speed
    speed += 1

  # Draw Game

  # Food
  pygame.draw.rect(window,red,(food_x,food_y,10,10))

  # Snake body
  for segment in snake_body:
    pygame.draw.rect(window,white,(segment[0],segment[1],10,10))

  # Update display
  pygame.display.update()

  # Control Frame Rate (Speed)
  clock.tick(speed)

# Quit game
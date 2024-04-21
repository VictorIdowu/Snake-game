import pygame
import random

pygame.init()

# Setting up game window
window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Setting up game variables
white = (255,255,255)
black = (0,0,0,0)
red = (255,0,0)

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
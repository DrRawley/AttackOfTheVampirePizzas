#Import Libraries
#import sys #checked to see what version of python was running where
#print(sys.executable)
import pygame
from pygame import *
from random import randint
from VampireSprite import *

#Initialize pygame
pygame.init()
#Set up clock
clock = time.Clock()

#Define constants
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

#Define rates
SPAWN_RATE = 360
FRAME_RATE = 60

#define tile parameters
WIDTH = 100
HEIGHT = 100

#Define colors
WHITE = (255,255,255)

#Create game window
GAME_WINDOW = display.set_mode(WINDOW_RES) #tuple data type
display.set_caption('Attack of the Vampire Pizzas!')

#add background image
background_img = image.load('gameassets/restaurant.jpg')
background_surf = Surface.convert_alpha(background_img)
BACKGROUND = transform.scale(background_surf, WINDOW_RES)
GAME_WINDOW.blit(BACKGROUND,(0,0))

#Setup enemy image
pizza_img = image.load('gameassets/vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (WIDTH,HEIGHT))

#Create a group for all the VampireSprite instances
all_vampires = sprite.Group()



#-----------------------------------------------------------------
#Initialize and draw bg grid
tile_color = WHITE
for row in range(6):
  for col in range(11):
    draw.rect(GAME_WINDOW, tile_color, (col*WIDTH,row*HEIGHT,WIDTH,HEIGHT), 1)
  


#-----------------------------------------------------------------
#Start Main Game Loop
game_running = True
#Game Loop
while game_running:
  # GAME_WINDOW.blit(BACKGROUND,(0,0))
  for row in range(6):
    for col in range(11):
      draw.rect(GAME_WINDOW, tile_color, (col*WIDTH,row*HEIGHT,WIDTH,HEIGHT), 1)
  #Check for events
  for event in pygame.event.get():

    #Exit loop on quit
    if event.type == QUIT:
      game_running = False
  
  #Spawn Vampire Pizza Sprites
  if randint(1, SPAWN_RATE) == 1:
    VampireSprite(VAMPIRE_PIZZA, all_vampires)
  #Update sprites
  for vampire in all_vampires:
    vampire.update(GAME_WINDOW, BACKGROUND)
  #Update display
  display.update()

  clock.tick(FRAME_RATE)

#End Main Game Loop
#-----------------------------------------------------------------
#Clean up game
pygame.quit()

#Import Libraries
import sys
#print(sys.executable)
import pygame
from pygame import *
from random import randint
from VampireSprite import *
from BackgroundTile import *

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
#Initialize and draw the background grid

#Create an empty list
tile_grid = []
tile_color = WHITE
for row in range(6):
  #Create an empty list each time the loop runs
  row_of_tiles = []
  #Add each of the six lists called row_of_tiles to the tile_grid list above
  tile_grid.append(row_of_tiles)
  for column in range(11):
    #Create an invisible rect for each background tile sprite
    tile_rect = Rect(column*WIDTH, row*HEIGHT, WIDTH, HEIGHT)
    #For each new column in each row create a new background tile sprite
    new_tile = BackgroundTile(tile_rect)
    #Add each new background tile sprite to the correct row_of_tiles list
    row_of_tiles.append(new_tile)
#Initialize and draw VISIBLE grid TO the background surface
for row in range(6):
  for column in range(11):
    draw.rect(BACKGROUND, tile_color, (column*WIDTH, row*HEIGHT, WIDTH, HEIGHT), 1)
GAME_WINDOW.blit(BACKGROUND,(0,0))


#-----------------------------------------------------------------
#Start Main Game Loop
game_running = True
#Game Loop
while game_running:
  #Check for events
  for event in pygame.event.get():

    #Exit loop on quit
    if event.type == QUIT:
      game_running = False
    #Listen for the mouse button to be clicked
    elif event.type == MOUSEBUTTONDOWN:
      #Get the x,y coordinates where the mouse was clicked on the screen
      coordinates = mouse.get_pos()
      x = coordinates[0]
      y = coordinates[1]
      #Find the background tile at the location where the mouse was clicked and
      #change the value of effect to True
      tile_y = y // 100
      tile_x = x // 100
      tile_grid[tile_y][tile_x].effect = True
      print('You clicked me! x: ' + str(x) + '  y: ' + str(y))
      print('This corresponds to tile: row: ' + str(tile_y) + '  col: ' + str(tile_x))
      sys.stdout.flush() #write debug stuff to console right away

  #Spawn Vampire Pizza Sprites
  if randint(1, SPAWN_RATE) == 1:
    VampireSprite(VAMPIRE_PIZZA, all_vampires)
  #Update sprites
  for vampire in all_vampires:
    vampire.update(GAME_WINDOW, BACKGROUND)
  #Update display
  #display.update()
  display.flip()

  clock.tick(FRAME_RATE)

#End Main Game Loop
#-----------------------------------------------------------------
#Clean up game
pygame.quit()

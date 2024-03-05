#Import Libraries
import sys
#print(sys.executable)
import pygame
from pygame import *
from random import randint
from VampireSprite import *
from Tiles import *
from Counters import *
from Trap import *

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

#Pizza bucks
STARTING_BUCKS = 15
BUCK_RATE = 120 #number of loops to earn a buck
STARTING_BUCK_BOOSTER = 1

#Define speeds
REG_SPEED = 2
SLOW_SPEED = 1

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

#Set up trap images
garlic_img = image.load('gameassets/garlic.png')
garlic_surf = Surface.convert_alpha(garlic_img)
GARLIC = transform.scale(garlic_surf, (WIDTH, HEIGHT))
cutter_img = image.load('gameassets/pizzacutter.png')
cutter_surf = Surface.convert_alpha(cutter_img)
CUTTER = transform.scale(cutter_surf, (WIDTH, HEIGHT))
pepperoni_img = image.load('gameassets/pepperoni.png')
pepperoni_surf = Surface.convert_alpha(pepperoni_img)
PEPPERONI = transform.scale(pepperoni_surf, (WIDTH, HEIGHT))


#Create a group for all the VampireSprite instances
all_vampires = sprite.Group()

#Create inital instances
counters = Counters(STARTING_BUCKS, BUCK_RATE, STARTING_BUCK_BOOSTER)
SLOW = Trap('SLOW', 5, GARLIC)
DAMAGE = Trap('DAMAGE', 3, CUTTER)
EARN = Trap('EARN', 7, PEPPERONI)
trap_applicator = TrapApplicator()

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
      #tile_grid[tile_y][tile_x].effect = True
      trap_applicator.select_tile(tile_grid[tile_y][tile_x], counters)
      # print('You clicked me! x: ' + str(x) + '  y: ' + str(y))
      # print('This corresponds to tile: row: ' + str(tile_y) + '  col: ' + str(tile_x))
      # sys.stdout.flush() #write debug stuff to console right away

  #Spawn Vampire Pizza Sprites
  if randint(1, SPAWN_RATE) == 1:
    VampireSprite(VAMPIRE_PIZZA, REG_SPEED, all_vampires)

  #Set up collision detection
  #Run through each vamp pizza sprite in the list
  for vampire in all_vampires:
    #Store the row where the vampire sprite is located
    tile_row = tile_grid[vampire.rect.y // 100]
    #Store the current location of the left edge of the vampire sprite
    vamp_left_side = vampire.rect.x // 100
    #Store the current location of the right edge
    vamp_right_side = (vampire.rect.x + vampire.rect.width) // 100
    #If the vampire sprite is on the grid, find which column it's in
    if 0 <= vamp_left_side <= 10:
      left_tile = tile_row[vamp_left_side]
    #Return no column if the vampire sprite is not on the grid
    else:
      left_tile = None
    #Do the same for the right side
    if 0 <= vamp_right_side <= 10:
      right_tile = tile_row[vamp_right_side]
    else:
      right_tile = None
    #Now test if the left side of the vampire pizza is touching a tile and
    #if that tile has been clicked.
    #if true, set the vampire speed to 1
    if bool(left_tile) and left_tile.effect:
      vampire.speed = SLOW_SPEED
    #Test if the right side is touching a tile and if that one has been clicked
    if bool(right_tile) and right_tile.effect:
      #Make sure both sides are touching a different tile
      if right_tile != left_tile:
        #if both are true, change vampire speed to 1
        vampire.speed = SLOW_SPEED
    #Delete the sprite if it leaves the screen
    if vampire.rect.x <= 0:
      vampire.kill()
    

  #Update vampire sprites
  for vampire in all_vampires:
    vampire.update(GAME_WINDOW, BACKGROUND)
  #Update pizza bucks counter
  counters.update(GAME_WINDOW,BACKGROUND,WHITE,WINDOW_RES)
  #Update display
  display.update()

  clock.tick(FRAME_RATE)

#End Main Game Loop
#-----------------------------------------------------------------
#Clean up game
pygame.quit()

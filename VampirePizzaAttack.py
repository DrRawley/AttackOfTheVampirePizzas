#Import Libraries
#import sys #checked to see what version of python was running where
#print(sys.executable)
import pygame
from pygame import *

#Initialize pygame
pygame.init()

#Define constants
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 400
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

#Create game window
GAME_WINDOW = display.set_mode(WINDOW_RES) #tuple data type
display.set_caption('Attack of the Vampire Pizzas!')

#Setup enemy image
pizza_img = image.load('gameassets/vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (100,100))
GAME_WINDOW.blit(VAMPIRE_PIZZA, (150,150))

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
  
  #Update display
  display.update()

#End Main Game Loop
#-----------------------------------------------------------------
#Clean up game
pygame.quit()

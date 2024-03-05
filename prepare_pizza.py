#Import Libraries
#import sys #checked to see what version of python was running where
#print(sys.executable)
import pygame
from pygame import *

#Initialize pygame
pygame.init()

#Define constants
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

#Create game window
GAME_WINDOW = display.set_mode(WINDOW_RES) #tuple data type
display.set_caption('Attack of the Vampire Pizzas!')

#draw pizza box
draw.rect(GAME_WINDOW, (160,82,45), (895,395,110,110), 5)
draw.rect(GAME_WINDOW, (160,82,45), (895,295,110,110), 0) #lid
#Setup enemy image
pizza_img = image.load('gameassets/vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (100,100))
GAME_WINDOW.blit(VAMPIRE_PIZZA, (900,400))

#Add a giant pepperoni
draw.circle(GAME_WINDOW, (255,0,0), (925,425), 25, 0)


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

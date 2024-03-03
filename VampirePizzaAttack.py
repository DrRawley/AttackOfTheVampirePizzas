#Import Libraries
#import sys #checked to see what version of python was running where
#print(sys.executable)
import pygame
from pygame import *

#Initialize pygame
pygame.init()

#Create game window
GAME_WINDOW = display.set_mode((900,400)) #tuple data type
display.set_caption('Attack of the Vampire Pizzas!')

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
  
    display.update()

#End Main Game Loop
#-----------------------------------------------------------------
#Clean up game
pygame.quit()

import pygame
from pygame import *
from random import randint

#Create a subclass of Sprite called VampireSprite
class VampireSprite(sprite.Sprite):
  #Define the VampireSprite setup method
  def __init__(self, SPRITE, SPEED, all_vampires):
    #Take all the behavior rules fromthe Sprite class and use them for VampireSprite
    super().__init__()
    #Set the default movement speed
    self.speed = SPEED
    #Randomly select a lane between 0 and 4
    self.lane = randint(0,4)
    #Add all vampire pizza sprites to a group called all_vampires
    all_vampires.add(self)
    #Use the VAMPIRE_PIZZA image as the image for vampire pizza sprites
    self.image = SPRITE.copy()
    #Set each sprite's y-coordinate at the middle of the selected lane
    y = 50 + self.lane * 100
    #Create a rect for each sprite and place it just off the right side of the screen in the correct lane
    self.rect = self.image.get_rect(center = (1100,y))
  #Draw the sprite
  from Counters import Counters
  def update(self, game_window, BACKGROUND, counters: Counters):
    #Erase the last sprite image
    game_window.blit(BACKGROUND, (self.rect.x, self.rect.y), self.rect)
    #Move the sprite
    self.rect.x -= self.speed
    #Update sprite image to new location
    game_window.blit(self.image, (self.rect.x, self.rect.y))
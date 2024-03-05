import pygame
from pygame import *

#Create a subclass of Sprite called BackgroundTile
class BackgroundTile(sprite.Sprite):
  #Define the BackgroundTile setup method
  def __init__(self, rect):
    super().__init__()
    self.effect = False
    self.rect = rect

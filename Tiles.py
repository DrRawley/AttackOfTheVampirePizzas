import pygame
from pygame import *
from Trap import *
from Counters import *

#Create a subclass of Sprite called BackgroundTile
class BackgroundTile(sprite.Sprite):
  #Define the BackgroundTile setup method
  def __init__(self, rect):
    super().__init__()
    self.effect = False
    self.trap = None
    self.rect = rect

#A subclass of BackgroundTile where the player can set traps
class PlayTile(BackgroundTile):
  #Set the trap on the slected play tile
  def set_trap(self, trap: Trap, counters: Counters):
    if bool(trap) and not bool(self.trap):
      counters.pizza_bucks -= trap.cost
      self.trap = trap
      if trap == 'EARN':
        counters.buck_booster += 1
    return None
  #Draw the trap image to the selected play tile
  def draw_trap(self, game_window, trap_applicator: TrapApplicator):
    if bool(self.trap):
      game_window.blit(self.trap.trap_img, (self.rect.x, self.rect.y))
      
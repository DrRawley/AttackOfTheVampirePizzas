import pygame
from pygame import *
from Counters import *

#Create a subclass of Sprite called BackgroundTile
class BackgroundTile(sprite.Sprite):
  #Define the BackgroundTile setup method
  def __init__(self, rect):
    super().__init__()
    self.effect = False
    from Trap import Trap
    self.trap: Trap = None
    self.rect = rect
  #If I do the type defs here I still get circular import erros
  def set_trap(self, trap, counters: Counters):
    raise NotImplementedError("Subclass must implement this method")
  def draw_trap(self, game_window, trap_applicator, WIDTH, HEIGHT):
    raise NotImplementedError("Subclass must implement this method")

#A subclass of BackgroundTile where the player can set traps
class PlayTile(BackgroundTile):
  def __init__(self, rect):
    super().__init__(rect)
  #Set the trap on the slected play tile
  from Trap import Trap #defered import --avoid circular import
  def set_trap(self, trap: Trap, counters: Counters):
    if bool(trap) and not bool(self.trap):
      counters.pizza_bucks -= trap.cost
      self.trap = trap
      from VampirePizzaAttack import EARN
      if trap == EARN:
        counters.buck_booster += 1
    return None
  #Draw the trap image to the selected play tile
  from Trap import TrapApplicator #defered import --avoid circular import
  def draw_trap(self, game_window, trap_applicator: TrapApplicator, WIDTH, HEIGHT):
    if bool(self.trap):
      game_window.blit(self.trap.trap_img, (self.rect.x, self.rect.y))

#Button Tile  --Tiles player clicks on to select trap
class ButtonTile(BackgroundTile):
  def __init__(self, rect):
    super().__init__(rect)
  from Trap import Trap
  def set_trap(self, trap: Trap, counters: Counters):
    if counters.pizza_bucks >= self.trap.cost:
      return self.trap
    else:
      return None
  from Trap import TrapApplicator
  def draw_trap(self, game_window, trap_applicator: TrapApplicator, WIDTH, HEIGHT):
    if bool(trap_applicator.selected):
      if trap_applicator == self.trap:
        draw.rect(game_window, (238,190,47), (self.rect.x, self.rect.y, WIDTH, HEIGHT), 5)

#Inactive Tile class --tiles that aren't part of the active game area
class InactiveTile(BackgroundTile):
  def __init__(self, rect):
    super().__init__(rect)
  from Trap import Trap
  def set_trap(self, trap: Trap, counters: Counters):
    return None
  from Trap import TrapApplicator
  def draw_trap(self, game_window, trap_applicator: TrapApplicator, WIDTH, HEIGHT):
    pass


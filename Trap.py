import pygame
from pygame import *
from Counters import *
from BackgroundTile import *

#Set up Trap class
class Trap(object):
  def __init__(self, trap_kind, cost, trap_img) -> None:
    self.trap_kind = trap_kind
    self.cost = cost
    self.trap_img = trap_img


#Set up TrapApplicator class
class TrapApplicator(object):
  def __init__(self) -> None:
    self.selected = None
  def select_trap(self, trap: Trap, counters: Counters):
    if trap.cost <= counters.pizza_bucks:
      self.selected = trap
  def select_tile(self, tile: BackgroundTile, counters: Counters):
    self.selected = tile.set_trap(self.selected, counters)
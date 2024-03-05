import pygame
from pygame import *

#Create Counters class
class Counters(object):
  #Set up init method
  def __init__(self, pizza_bucks, buck_rate, buck_booster) -> None:
    #Start game loop counter at 0
    self.loop_count = 0
    #Set up the look of the counter on the screen
    self.display_font = font.Font('gameassets/pizza_font.ttf', 25)
    #Define the pizza_bucks attribute using the pizza_bucks argument
    self.pizza_bucks = pizza_bucks
    #Define the buck_rate attribute using the buck_rate argument
    self.buck_rate = buck_rate
    #Define the buck_booster attribute using the buck_booster argument
    self.buck_booster = buck_booster
    #Initialize a rect
    self.bucks_rect = None
  #Increase player's bucks based on time passing
  def increment_bucks(self):
    #Add a set number of pizza bucks to the total once every 120 loops
    #about once every 2 seconds
    if self.loop_count % self.buck_rate == 0:
      self.pizza_bucks += self.buck_booster
  #Define update method
  def update(self, game_window, BACKGROUND, COLOR, WINDOW_RES):
    self.loop_count += 1
    self.increment_bucks()
    self.draw_bucks(game_window, BACKGROUND, COLOR, WINDOW_RES)
  #Method to draw pizza bucks to the window
  def draw_bucks(self, game_window, BACKGROUND, COLOR, WINDOW_RES):
    #Erase the last number from the window
    if bool(self.bucks_rect):
      game_window.blit(BACKGROUND, (self.bucks_rect.x, self.bucks_rect.y), self.bucks_rect)
    bucks_surf = self.display_font.render(str(self.pizza_bucks), True, COLOR)
    #create a rect for bucks_surf
    self.bucks_rect = bucks_surf.get_rect()
    self.bucks_rect.x = WINDOW_RES[0] - 50
    self.bucks_rect.y = WINDOW_RES[1] - 50
    #display the new pizza bucks total
    game_window.blit(bucks_surf, self.bucks_rect)

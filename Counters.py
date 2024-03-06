import pygame
from pygame import *

#Create Counters class
class Counters(object):
  #Set up init method
  def __init__(self, pizza_bucks: int, buck_rate: int, buck_booster: int, WIN_TIME: int) -> None:
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
    #Initialize a timer
    self.timer = WIN_TIME  #this doesn't seem to be used anywhere
    self.timer_rect = None
    #Bad reviews
    self.bad_reviews = 0
    self.bad_rev_rect = None
  #Increase player's bucks based on time passing
  def increment_bucks(self):
    #Add a set number of pizza bucks to the total once every 120 loops
    #about once every 2 seconds
    print(self.buck_booster)
    import sys
    sys.stdout.flush()
    if self.loop_count % self.buck_rate == 0:
      self.pizza_bucks += self.buck_booster
  #Define update method
  def update(self, game_window: Surface, BACKGROUND: Surface, COLOR: tuple[int, int, int], WINDOW_RES: tuple[int, int], WIN_TIME: int, FRAME_RATE: int):
    self.loop_count += 1
    self.increment_bucks()
    self.draw_bucks(game_window, BACKGROUND, COLOR, WINDOW_RES)
    self.draw_bad_reviews(game_window, BACKGROUND, COLOR, WINDOW_RES)
    self.draw_timer(game_window, BACKGROUND, COLOR, WINDOW_RES, WIN_TIME, FRAME_RATE)
  #Method to draw pizza bucks to the window
  def draw_bucks(self, game_window: Surface, BACKGROUND: Surface, COLOR: tuple[int, int, int], WINDOW_RES: tuple[int, int]):
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
  #Method to draw the bad reviews
  def draw_bad_reviews(self, game_window: Surface, BACKGROUND: Surface, COLOR: tuple[int, int, int], WINDOW_RES: tuple[int, int]):
    #Test if there are bad reviews and erase the old number if there is
    if bool(self.bad_rev_rect):
      game_window.blit(BACKGROUND, (self.bad_rev_rect.x, self.bad_rev_rect.y), self.bad_rev_rect)
    #font and color to use in the display
    bad_rev_surf = self.display_font.render(str(self.bad_reviews), True, COLOR)
    #set up a rect so that we can interact with the number
    self.bad_rev_rect = bad_rev_surf.get_rect()
    #put the display in the second to last col and bottom row
    self.bad_rev_rect.x = WINDOW_RES[0] - 150
    self.bad_rev_rect.y = WINDOW_RES[1] - 50
    #Display the number to the screen
    game_window.blit(bad_rev_surf, self.bad_rev_rect)
  #Method to draw time
  def draw_timer(self, game_window: Surface, BACKGROUND: Surface, COLOR: tuple[int, int, int], WINDOW_RES: tuple[int, int], WIN_TIME: int, FRAME_RATE: int):
    if bool(self.timer_rect):
      game_window.blit(BACKGROUND, (self.timer_rect.x, self.timer_rect.y), self.timer_rect)
    timer_surf = self.display_font.render(str((WIN_TIME - self.loop_count)//FRAME_RATE), True, COLOR)
    self.timer_rect = timer_surf.get_rect()
    self.timer_rect.x = WINDOW_RES[0] - 250
    self.timer_rect.y = WINDOW_RES[1] - 50
    game_window.blit(timer_surf, self.timer_rect)

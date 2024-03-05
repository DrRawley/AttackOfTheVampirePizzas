from monster import *

#Create an instance of Monster
# my_monster = Monster('Spooky Snack')
#Call the methods on the new instance
# my_monster.speak()
# my_monster.eat('food')
# my_monster.eat('mutton')

#Create an Instance of FrakenBurger
# my_frankenburger = FrankenBurger('Veggiesaurus')
#Call the methods
# my_frankenburger.speak()
# my_frankenburger.eat('pickles')
# my_frankenburger.eat('hamburger patties')

#Create an Instance of CrummyMummy
# my_crummymummy = CrummyMummy('Crumbly')
#Call the methods
# my_crummymummy.speak()
# my_crummymummy.eat('chocolate chips')

#Create an instance of WereWatermelon
# my_werewatermelon = WereWatermelon('BigJubblies')
#Call the methods
# my_werewatermelon.speak()
# my_werewatermelon.eat('watermelon juice')

monster_selection = input('What kind of monster do you want to create?\nSelect:\n 1) frankenburger\n 2) crummymummy\n 3) werewatermelon.\n>>')
monster_name = input('What do you want to name your monster?\n>>')
if monster_selection == '1':
  my_monster = FrankenBurger(monster_name)
elif monster_selection == '2':
  my_monster = CrummyMummy(monster_name)
elif monster_selection == '3':
  my_monster = WereWatermelon(monster_name)
else:
  print('Invalid selection, a monster will eat YOU now.')
  exit()

my_monster.speak()

monster_meal = input('What will you feed your monster?\n>>')
my_monster.eat(monster_meal)


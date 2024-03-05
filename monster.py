#Create the superclass
class Monster(object):
  #Set up the class attribute, the same for all instances
  eats = 'food'
  #Define the __init__ method
  def __init__(self, name) -> None:
    self.name = name
    pass
  #Define a method for speaking behavior
  def speak(self):
    print(self.name + ' speaks.')
    pass
  #Define a method for eating behavior
  def eat(self, meal):
    if meal == self.eats:
      print('Yum!')
    else:
      print('Blech!')
    pass
##End class def
  
#Create subclasses of Monster
class FrankenBurger(Monster):
  #Set up the class attribute
  eats = 'hamburger patties'
  #Define any methods that are different
  def speak(self):
    print('My name is ' + self.name + ' Burger.')
    pass

class CrummyMummy(Monster):
  eats = 'chocolate chips'
  def speak(self):
    print('My name is ' + self.name + ' Mummy.')

class WereWatermelon(Monster):
  eats = 'watermelon juice'
  def speak(self):
    print('My name is Were' + self.name + '.')

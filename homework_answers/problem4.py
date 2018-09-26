from problem3 import Animal

class Penguin(Animal):
  def __init__(self):
    super().__init__()
    print('I am a penguin!')
    self.energy = 100

  def move(self):
    self.energy -= 5
    print('I am sliding!')

class Eagle(Animal):
  def __init__(self):
    super().__init__()
    print('I am an eagle!')
    self.energy = 20

  def move(self):
    if self.energy < 0: 
      print('I\'m too tired to fly…')
    else:
      self.energy -= 20

  def say_hi(self):
    print('shrieeeeeek!')


animal = Animal()
animal.get_status()
animal.eat(60)
animal.get_status()
animal.move()
animal.get_status()
animal.say_hi()
print()

penguin = Penguin()
penguin.eat(5)
penguin.get_status()
penguin.move()
penguin.get_status()
penguin.say_hi()
print()

eagle = Eagle()
eagle.say_hi()
eagle.get_status()
eagle.move()
eagle.get_status()
eagle.move()
eagle.get_status()
eagle.move()
print()
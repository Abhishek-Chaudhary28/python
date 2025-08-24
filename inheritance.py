class Person:
  def rest(self):
    print("Rest heals 10 points ")
  def move(self):
    print("Moves 4 pace ")

# Single Level Inheritance
class Doctor(Person):
  def heal (self):
    print("Doctor heals 20 points : ")


#Multi Level Inheritance
class Wizard(Person,Doctor):
  def heal(self):
    print("wizard can heal 20 points more ")

# Hierarchical inheritance
class Fighter(Person):
  def fight(self):
    print("Fighter damage 10 points : ")
  def move(self):
    print("Fighter damage 10 pace : ")
    

action= Wizard()
action.rest()
action.heal()
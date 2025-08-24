class Pizza :
  def __init__(self,size,crust_type,toppings=None):
    self.size = size
    self.crust_type = crust_type
    self.toppings = toppings if toppings else []

  def add(self,topping):
    self.toppings.append(topping)

  def remove(self,topping):
    if topping in self.toppings:
      self.toppings.remove(topping)
    else:
      print(f"{topping} isnt in your topping")

  def describe_pizza(self):
    print(f"Pizza Size : {self.size.title()} type : {self.crust_type.title()} ")
    if self.toppings:
      print ("Toppings : ")
      for topping in self.toppings:
        print(f" :  {topping}")
    else:
      print("No toppings added yet")

custom = Pizza("Large","Thin")   
custom.add("Pep")
custom.add("onion")
custom.add("Mush")
custom.remove("Mush")
custom.describe_pizza()

friend_pizza = Pizza("medium", "deep dish", ["bacon", "extra cheese"])
friend_pizza.add("olives")      #line 7  method call
friend_pizza.remove("Other")    #line 14 method call
friend_pizza.describe_pizza()   #line 16 method call
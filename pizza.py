class Pizza:
  def __init__(self,size,crust_type,topping=None):
    self.size =size
    self.crust = crust_type
    self.topping = topping if topping else []

  def add(self,topping):
    self.topping.append(topping)

  def remove(self,topping):
    if topping in self.topping:
      self.topping.remove(topping)
    else:
      print(f"{topping} isnt in your topping")

  def nprint(self):
    if self.topping:
      topping_str = ", ".join(self.topping)
    else:
      topping_str = "No Topping yet ! "
    print(f"Pizza Size : {self.size} type : {self.crust} and the tooping is {topping_str}")

size = input("Enter Large, Medium, Small : ").strip()
crust_type = input("Enter Thin, Medium, Thick : ").strip()
intput_topping = input("Enter Peporine, onion, olive Leave empty for none: ").strip()
topping = [t.strip() for t in intput_topping.split(",")] if intput_topping else []

custom = Pizza(size, crust_type, topping)
custom.nprint()
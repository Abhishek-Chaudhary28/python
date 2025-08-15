#Coffee Order Challenge
totalPrice = 0
drinkCount = 0

while True:
  name = input("Enter you name : ")

  if name == "done":
    break
  
  drink = input("Enter the drink name : ")

  if drink == "latte":
    totalPrice += 3.50
    drinkCount += 1
  
  elif drink == "tea":
    totalPrice += 3.00
    drinkCount += 1

  elif drink == "water":
    totalPrice += 2.50
    drinkCount += 1

  else:
    print(f"Sorry {drink} not avilable ")

print(f"Total drink ordere : ",drinkCount)
print(f"Total price : ",totalPrice)


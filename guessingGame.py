import random

num = random.randint(1, 100)
guess_counter = 0 
guess_limit = 5


while guess_counter < guess_limit:
  guess1 = int(input("Enter the number from 1 - 100: "))    
  if guess1 == num:
    print(f"you guessed it right {guess1} is the number")
    break
  else: 
    if guess1 > num:
      print(f"You have guess it more  GUESS AGAIN! ")
    else: 
      print(f"you guessed it low GUESS AGAIN! ")
    guess_counter+=1
if guess_counter == guess_limit:
  print(f"Sorry you have used all chances Right answer is {num} try again")
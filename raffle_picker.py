# 🏆 Raffle Prize Picker — Challenge Steps
#
# 1. Ask how many people are entering the raffle (at least 3 names).
# 2. Use a loop to collect their names into a list.
# 3. Ask for exactly 3 prize names (in order) and store them in a list.
# 4. Randomly pick 3 different winners from the participant list.
# 5. Print out who wins which prize and make sure the final one
#    is clearly marked as the Grand Prize. 🏆
#
# Hint: Use loops, lists, and a tool that picks random items without repeats.
import random
userno = int(input("Enter the number of participant in Raffle : "))
if userno < 3:
  print("Number of participant should be at least 3")
  exit()

user = []
for i in range(userno):
  a = str(input(f"Enter the name of participant --> {i+1}:"))
  user.append(a)

maxprize = 3
prize = []
for i in range(maxprize):
  a = str(input(f"enter the prize name #{i+1}: "))
  prize.append(a)


winner = random.sample(user,3)

print("======= Raffle Winner ======")
for i in range(3):
  if i==2:
    print(f"Grand Prize :{winner[i]}  wins the {prize[i]}")
  else:
    print(f"winners {winner[i]} wins the {prize[i]}")


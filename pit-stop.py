totaltime = float(input("Enter the total time to complete the race : "))
pits = int(input("How many pits are there : "))
avgpitstop = float(input("Enter the average pit stop time : "))

totalpitstop = avgpitstop * pits 
percent = (totalpitstop/totaltime  )*100
percent = round(percent, 2)

print(totalpitstop)
print(percent)

if percent > 5:
  print("You need a new pit crew ")
else:
  print("Your pit crew is good")
  
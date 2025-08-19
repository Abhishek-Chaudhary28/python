
seatnumber = {1 : {"name" : 'rocky',"breed" : "german", "pickuptime" : 10,"dropoff": 11},2 :{"name" : "boss",'breed' : "indain", "pickuptime" : 12,"dropoff": 3}}
max_seats = 3

for seat, info in seatnumber.items():
  print(f'Seat No : {seat} and Name : {info["name"]} and pickup time is {info["pickuptime"]}')

if len(seatnumber) <= max_seats:
  newseat = len(seatnumber) + 1
  newpet = {
      "name" : input("\nEnter the name of new pet : ").strip(),
      "breed" : input("Enter the breed of new pet: ").strip(),
      "pickuptime" : input("Enter the pickup time : "),
      "dropoff": input("Enter the drop off time : ")
      }
  seatnumber[newseat] = newpet
  print(f"Hello {newpet['name']} your seat number is {newseat} \n")
else: 
  print("Limit Reached")

for seat, info in seatnumber.items():
  print(f'Seat No : {seat} and Name : {info["name"]} and pickup time is {info["pickuptime"]}')

leave = int(input("\nSeat Number of pet who want to leave : "))
if leave in seatnumber.keys():
  leaved = seatnumber.pop(leave)

  print(f"👋  {leaved['name']} (seat {leave}) heads home early.\n")

for seat, info in seatnumber.items():
  print(f'Seat No : {seat} and Name : {info["name"]} and pickup time is {info["pickuptime"]}')

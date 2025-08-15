mission_1_speed = 40000  # Pathfinder
mission_2_speed = 75000  # Perseverance
mission_3_speed = 120000 # Starship

mars_distance = 225_000_000  # in kilometers
fuel_rate = 0.3              # liters per kilometer
fuel_price = 1.8             # dollars per liter

def travel_time(distance,speed):
  return round(distance/speed)

def mission_cost(distance,fuel_price, fuel_rate):
  return round(distance* fuel_price * fuel_rate)

# Helper function to convert hours to days and hours
def format_time(hours):
    days = hours // 24
    rem_hours = hours % 24
    return f"{days} days {rem_hours} hours"

time1 = travel_time(mars_distance,mission_1_speed)
cost_1 = mission_cost(mars_distance,fuel_price,fuel_rate)

time2 = travel_time(mars_distance,mission_2_speed)


time3 = travel_time(mars_distance,mission_3_speed)


print(f"PathFinder travel time is  {time1} hours ({format_time(time1)}) and the total fuel cost is {cost_1} ")
print(f"Perseverance travel time is  {time2} hours  ({format_time(time2)}) and the total fuel cost is {cost_1} ")
print(f"Starship travel time is  {time3} hours  ({format_time(time3)}) and the total fuel cost is {cost_1} ")
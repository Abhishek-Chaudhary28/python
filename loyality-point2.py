def earn_points(price):
  points = 3 * int(price)
  return points

def tier_label(points):
  if points <= 100:
    return "Bronze"
  elif points < 500:
    return "Silver"
  elif points >= 500:
    return "Gold"

spent =  [3.75, 7.20, 19.99, 100, 56.50]
total_spent = 0.0
total_point = 0

for amount in spent:
  total_spent += amount
  total_point += earn_points(amount)

final_tier = tier_label(total_point)  

print("Loyality Summary")
print(f"Total dollar spent : {total_spent}")
print(f"Total points Earn : {total_point}")
print(f"Total Final Tier : {final_tier}")
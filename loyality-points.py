# ☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier

# Purchase history (e.g., 3.75, 7.20, etc.)

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
total_spent = sum(spent)
total_point = sum(earn_points(amount) for amount in spent)

print("Loyality Summary")
print(f"Total dollar spent : {total_spent}")
print(f"Total points Earn : {total_point}")
print(f"Total Final Tier : {tier_label(total_point)}")

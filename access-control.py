# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

revoked = {2, 4, 6, 8}

aproved = []
denied = []

while True :
  name = input("Enter Name: ")
  if name == 'done':
    break

  badge = int(input("Enter your bagde no : "))

  if badge in revoked:
    denied.append(name)
    print("Access Denied")
  else:
    aproved.append(name)
    print('Access Granted')
    

sorted(aproved)
print(f"Approved Visitors : {aproved}")

sorted(denied)
print(f"Denied Visitors : {denied}")

print(f"Total aprroved : {len(aproved)}")
print(f"Total denied : {len(denied)}")
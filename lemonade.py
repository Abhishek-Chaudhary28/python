sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

new_day = input("Enter the No of the lemon for new day : ")

sales_w2.append(int(new_day))
sales = sales_w1 + sales_w2

worstsales = min(sales) * 1.5
bestsales = max(sales) * 1.5


print(f"Combined sales: {worstsales + bestsales}")
print(f"Worst sales: {worstsales}")
print(f"Best sales: {bestsales}")
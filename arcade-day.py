cname = "Abhi"
npass = 10
token = 2
price = 50
reqtoken = 2

totaltoken = npass * token
cost = npass * price
gavail = totaltoken / reqtoken

print(f"{cname} has bought {npass} passes that will be {totaltoken} tokens and the price is {cost}")
print(f"Games available: {gavail}")

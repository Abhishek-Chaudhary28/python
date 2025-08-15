print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

mode = input("Chosse mode : + - * /  celsius to fahrenheit")
num1 = float(input("Enter first number : "))
if mode == 'cf':
  print(f"{num1} Celsius in fahrrenheit is {num1*9/5 +32}" )
else :
  num2 = float(input("Enter second number : "))


if mode == '+':
  print(num1 + num2)
elif mode == '-':
  print(num1 - num2)
elif mode == '*':
  print(num1 * num2)
elif mode == '/':
  print(num1 / num2)
else:
  print("Input error")

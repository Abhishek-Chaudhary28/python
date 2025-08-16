# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."

number = input("Enter the number : ")
number = number.strip()

for i in ['-',' ','.',',','(',')']:
  number = number.replace(i,' ')

chunk = number.split()
clean_no = ''.join(chunk)

if len(clean_no) == 10:
  print(f'({clean_no[0:3]})  {clean_no[3:6]} - {clean_no[6:10]} ')
else:
  print("Please enter exactly 10 digits.")


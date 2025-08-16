names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
name0 = names + names1                              #concatenate the names and names1
        
to_addnames = int(input("How many names do you want to add? :  "))  # take input for how many names to add
for index in range(to_addnames):
  name0.append(input("Enter new name :  "))        # take input to add name in list and add new name in the list 

for i in name0:
  print(f'{i.capitalize()} ! you are invited on sunday')
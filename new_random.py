import random
print(random.random())

for i in range(5):
  print(random.random()*6)

for i in range(5):
  print(random.uniform(1,6))

for i in range(5):
  print(random.randrange(1,100,10))

friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.choice(friends_list))
print(random.sample(friends_list,5))
print(random.shuffle(friends_list))
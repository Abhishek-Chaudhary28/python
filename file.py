my_file = open('text.txt', 'r')
#print(my_file.read())
#print(my_file.read(10))
print(my_file.readline())   

line_by_line = my_file.readlines()

print(line_by_line)
my_file.close()

with open('friend.csv','r') as f:
    friends = f.read().splitlines()
    print(friends)
    print(friends)
    for friend in friends:
        friend = friend.split(',')
        name = friend[0]
        year = int(friend[1].strip())
        print(f'In 2030 {name} will be {2030 -year} years old')
f.close()

with open('movies.txt','r') as f:
    for line in f:
        print(line)
f.close()
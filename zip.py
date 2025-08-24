nums = [1,2,3,4]
letters = ['a','b','c','d','e']
names =['John','Eric', 'Anon','Joe']
combo =zip(nums,letters)
print(list(combo))

nums = '1234'
letters = ['a','b','c','d','e']
names =['John','Eric', 'Anon','Joe']
combo1 =list(zip(nums,letters,names))
print((combo1))

#UNzipping
num,let,nam = zip(*combo1)
print(num,let,nam)

#Special Case
keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'
keys = keys.split()
values = values.split()
print(keys,values)

zip_dic = dict(zip(keys,values))
print(zip_dic)

# dictionary comprehnesion
new_dict = {key:value for key,value in zip(keys,values)}
print(new_dict)

# dictionary keys and values 
en,sv = list(zip_dic.keys()), list(zip_dic.values())
print(en,sv)

# Unzip all items turn into tuples
en1,sv1 = zip(*zip_dic.items())
print(en1,sv1)
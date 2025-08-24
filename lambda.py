print("Lambda Function")
def square (x):
  return x*x
# name = lambda parametrers(s): expression

square1 = lambda x: x*x
print(square1(6))

def name_and_alias(name,alias):
  return name.strip().title() + ':' + alias.strip().title()
print(name_and_alias("John","Cena"))

# name = lambda parametrers(s): expression
name_and_alias1 = lambda name,alias: name.strip().title() + ':' + alias.strip().title() 
print(name_and_alias1("Kukor","Cena"))

# oneline function definition
def name_and_alias2(name,alias) : return name.strip().title() + ':' + alias.strip().title() 
print(name_and_alias2("Third","Cena"))


monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']
def sort_names(name):
    return name.split(' ')
monty_python.sort(key = lambda name:name.split(' ')[-1])
print(monty_python) #alphabetical by last name.
monty_python.sort(key= sort_names)
print(monty_python) #sort in alphabetical by first name (then middle, then last).

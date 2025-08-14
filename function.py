def greeting(name, age):
    print("Hello "+name+ ", welcome to the program! you are "+age+"old")
    print(f"Hello {name}, welcome to the program! you are {age} old")

greeting("Abhi", "45")

#default greeting function
def greeting(name="User", age="18"):
    print("Hello "+name+ ", welcome to the program! you are "+str(age)+" old")
    print(f"Hello {name}, welcome to the program! you are {age} old")

greeting()

#input greeting function
def greeting(name="User", age="18"):
    print("Hello "+name+ ", welcome to the program! you are "+age+" old")
    print(f"Hello {name}, welcome to the program! you are {age} old")
name=input("Enter your name: ")
age=input("Enter your age: ")
greeting(name, age)

a = 7
b = 3
print(f"Equal : {a==b}")
print(f"Not Equal : {a!=b}")
print(f"More than : {a > b}")
print(f"less then : {a < b}")
print(f"less than equal : {a <= b}")
print(f"more then Equal : {a >= b}")
print(f"In Operator finds o in John : {'o' in 'John'}")

c = [3,7,42]
d = c
print(f"equal : {c == d}")
print(f'is opertor : {c is d}')
print(f"id operator : {id(c), id(d)}")   #memory id here 

print(int(True))
print(int(False))

print(bool(0))          # False
print(bool([]))         # empty list is False
print(bool(1))          # True
print(bool([1, 2, 3]))  # non-empty list is True
def func(n):
  return lambda a: a*n
doubler = func(2)
print(doubler(4))

print(type(func(5)))

def price_calc(cost,rate):
  return lambda hour: cost + rate*hour

totalcost= price_calc(10,20)
print(totalcost(2))

print((lambda a,b,c:a+b+c)(2,3,5) )
print((lambda a,b,c=2:a+b+c)(2,3,5) )
print((lambda a,b,c=2:a+b+c)(2,c=3,b=6))
print((lambda *args:sum(args))(1,2,3,4,5))

ghost = lambda a : a * a
print(ghost(5))
print('Lambdas Exercise')

# def f(x): return x + 5
f = lambda x : x+5
print(f(2))


from posixpath import split
print('Lambdas Exercise')


# def strip_spaces(str):
#    return ''.join(str.split(' '))

g = lambda str :  ''.join(str.split(' '))
print(g('Monty Pythons Flying Circus')) 


print('Lambdas Exercise')

def join_list_no_duplicates(list_a,list_b):
   return list(set(list_a + list_b))
list_a = [1,2,3,4]
list_b = [3,4,5,6,7]
#write lambda below 
join_list_no_duplicates1 = lambda list_a,list_b : list(set(list_a + list_b))
#join_list_no_duplicates = ...
print(join_list_no_duplicates1(list_a,list_b))


# lambda function in a function
print('Lambdas Exercise')

#Complete the function so it returns a function
def create_quad_func(a,b,c):
    # '''return function f(x) = ax^2 + bx + c'''
    return lambda x: a *x *x + b*x +c
f = create_quad_func(2,4,6)
g = create_quad_func(1,2,3)
print(f(2))
print(g(2))


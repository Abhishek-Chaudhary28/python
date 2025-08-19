def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
          return False
    return True

for i in range(1,101):
  if is_prime(i):
    print(f'Prime ')
  elif i % 3 == 0 and i % 5==0:
    print (f'FizzBuzz')
  elif i % 3 ==0:
    print(f'Fizz ')
  elif i % 5 == 0:
    print(f'Buzz ')
  else :
    print(i)

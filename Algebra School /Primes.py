#Looking if a number is a prime number an returning a boolean
def is_prime_number(x):
  if x <= 1:
    return False
  for i in range(2,x):
    if x % i == 0:
      return False
  return True


#We can also create a Function to give us all prime numbers in a specific range stored in a list
def prime_in_range(startrange,endrange):
  listofprimes = []

  for i in range(startrange,endrange):
    if is_prime_number(i)== True:
      listofprimes.append(i)
    else:
      pass
      
  return listofprimes

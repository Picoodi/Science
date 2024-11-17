#A function to convert decimals into a fraction which is stored as a tuple not fully shortened
#The return is in the form (numerator, denominator)
def decimals_to_fraction(decimal: str):
  exponent = int(len(decimal))-1
  number = float(decimal)
  numerator = int(number*10*exponent)
  denominator = 10*exponent
  return numerator, denominator



def decimals_to_fraction(decimal: str):
  exponent = int(len(decimal))-1
  number = float(decimal)
  numerator = int(number*10*exponent)
  denominator = 10*exponent
  return numerator, denominator


#A test function
def test(decimal, solution):      
    answer = decimals_to_fraction(str(decimal))
    if answer == solution:
        print("TEST PASSED")
    else:
        print("NOT PASSED")

#PROBLEM: THE WORKING WITH DECIMALS DOESNT WORK SO GOOD IN PYTHON NEEDS TO BE FIXED

#A function to convert decimals into a fraction which is stored as a tuple
#eg for making solutions look better

def decimals_to_fraction(decimal: str):
  exponent = int(len(decimal))-1
  number = float(decimal)
  numerator = int(number*10*exponent)
  denominator = 10*exponent
  return numerator, denominator



#TEST CODE
#x = 0.1 and y = 0.7 x+y= 0.8
x= 0.1
y= 0.7
equation = x+y
print(x+y)

solution = decimals_to_fractions(str(equation))
print(solution[0], "/", solution[1])

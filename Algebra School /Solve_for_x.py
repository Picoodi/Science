import sympy
from sympy import *

#The function takes an equation with a variable x and no else variables, solves after x and returns the solution
def solve_for_x(equation):
  x = symbols("x")
  solution = solve(equation,x)
  return solution





#A little test code.
#the equation x^2 -4 has the solutions x1 = -2 and x2 = 2.
eq = x**2 -4
if solve_for_x(eq) == [-2,2]:
  print("Test passed, right solution calculated")
else:
  print("Test failed, calculated wrong")  

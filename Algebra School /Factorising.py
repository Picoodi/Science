import sympy

#This Function Factorises an input equation if possible and returns it 
def factoring(equation):
  #We create a list with the alphabet so equations with all variables work
  var("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z")
  solution = sympy.factor(equation)
  return solution



def test(equation, solution):
  if equation == solution:
    print("Test passed, right solution calculated")
  else:
    print("Test failed, calculated wrong")
  

test(2*x+10*y+4*z, 2*(x+5*y+2*z))
test(2*x +10*y +3, 2*x +10*y +3)

#NST durch Newton Verfahren

xnew = -1
Abweichung = 0.0001

def function(x)-> float:
  fx= x**5+x**3+1
  return fx


def derivation(x) -> float:
  fxstrich = 5*x**4+3*x**2
  return fxstrich


def difference(xold, xnew) -> float:
  Differenz = xold - xnew

  if Differenz < 0:
    Differenz = Differenz * -1

  return Differenz

while derivation(xold,xnew) > Abweichung:
  xold = xnew
  xnew = xold - function(xold)/derivation(xold)

else:
  print("ungefähre NST bei",xnew)

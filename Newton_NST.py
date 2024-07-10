#NST durch Newton Verfahren

xnew = -1
Abweichung = 0.0001

def funktion(x)-> float:
  fx= x**5+x**3+1
  return fx


def ableitung(x) -> float:
  fxstrich = 5*x**4+3*x**2
  return fxstrich


def abweichung(xold, xnew) -> float:
  Differenz = xold - xnew

  if Differenz < 0:
    Differenz = Differenz * -1

  return Differenz

while abweichung(xold,xnew) > Abweichung:
  xold = xnew
  xnew = xold - funktion(xold)/ableitung(xold)

else:
  print("ungefähre NST bei",xnew)
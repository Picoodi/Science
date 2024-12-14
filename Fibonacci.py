#Fibonacci Sequence
def Fibonacci(n):
    if n < 0:
        print("Not a valid input range")
    elif n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]

    elif n > 2:
        Fibonacci = [0,1]
        for i in range(1,n-1):
            Fibonacci.append(Fibonacci[i] + Fibonacci[i-1])

        return Fibonacci



  


###Test#Code###
if Fibonacci(0) == []:
    print("Test 1 passed")
else:
    print("Test 1 failed")

if Fibonacci(2) == [0,1]:
    print("Test 2 passed")
else:
    print("Test 2 failed")

if Fibonacci(4) == [0,1,1,2,3,5,8]:
    print("Test 3 passed")
else:
    print("Test 3 failed")

if Fibonacci(10) == [0,1,1,2,3,5,8,13,21,34]:
    print("Test 4 passed")
else:
    print("Test 4 failed")

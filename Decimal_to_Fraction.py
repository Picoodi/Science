#we now gonna convert decimals into fractions
digit = input("Enter a decimal number to convert: ")

#now we look if its hundretz or thounandth and so on and get the exponent with it
#-1 because the string takes the . as a charakter
exponent = int(len(digit))-1

number = float(digit)

#we use the exponent to get the numerator
numerator = int(number*10**exponent)
denominator = 10**exponent

percent = number * 100

#output
print("The decimal is", number)
print("The fraction is", numerator, "/", denominator)
print("The percent is", percent, "%")
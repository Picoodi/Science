#imports of the libraries
import math

#constants
c = 299792 #Lightspeed in km/s



#function for calculating gamma
def gamma():
    print("Your velocity in km/s plz:")
    velocity = float(input())
    print("Your gamma:")
    gamma_solution = 1 / math.sqrt(1-(velocity/c)**2)
    print(gamma_solution)



#function for calculating velocity
def velocity():
    print("Your gamma plz:")
    gamma = float(input())
    print("Your Velocity")
    velocity_solution = math.sqrt(1-(1/gamma**2))*c
    print(velocity_solution)
    
 #function that calculates how much of a change of lifetime it would be for a human of 83 years in relativity to a system with factor 0   
def human():
    print("Your gamma plz:")
    gamma = float(input())
    years = (gamma - 1)*83
    days = (gamma - 1)*83*365
    hours = (gamma - 1)*83*365*24
    minutes = (gamma - 1)*83*365*24*60
    seconds = (gamma - 1)*83*365*24*60*60

    print("The Human lifetime would change about:")
    print(years, "years or")
    print(days, "days or")
    print(hours, "hours or")
    print(minutes, "minutes or")
    print(seconds, "seconds")
    print("to a system with the factor 0")


#asking the user what he is looking for
def asking():
    print()
    print("What are you looking for?")
    print("Type 1 for gamma and type 2 for velocity and 3 for how much time that would be for an average human time span of 83 years :")
    
    user = int(input())
    
    if user == 1:
        gamma()
    elif user == 2:
        velocity()
    elif user == 3:
        human()
    else:
        print("Sry dont know what you want")
        


#programm
while True:
    asking()

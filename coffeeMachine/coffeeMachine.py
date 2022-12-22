from menu_data import MENU, resources
from art import coffeecup

#print(coffeecup)

shouldStayOn = True

def printReport():
    waterLevel = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water:  {waterLevel}ml\nMilk: {milk}ml\nCoffee: {coffee}g\n" 
    
    

def responseToInput(userCoffeeChoice):
    if (userCoffeeChoice == "espresso"):
        print("Espresso made")
    elif(userCoffeeChoice =="latte"):
        print("latte made")
    elif(userCoffeeChoice == "capuccino"):
        print("capucinno made")
    elif(userCoffeeChoice == "report"):
        print(printReport())
    elif (userCoffeeChoice == "off"):
        quit()
    else:
        print("Incorrect choice")
        
        
while shouldStayOn:
            
    userCoffeeChoice = input("What would you like? (espresso/latte/capuccino): ")

    responseToInput(userCoffeeChoice)


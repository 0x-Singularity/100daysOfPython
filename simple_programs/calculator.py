import blackjackGame.art as art

print(art.logo)

def addition (numberOne, numberTwo):
    return numberOne + numberTwo 
    

def subtraction (numberOne, numberTwo):
    return numberOne - numberTwo 
  

def multiplication (numberOne, numberTwo):
    return numberOne * numberTwo 
    

def division (numberOne, numberTwo):
    return numberOne / numberTwo 


operations = {"+":addition, "-":subtraction, "*":multiplication, "/":division}


    

print("Hello, welcome to the calculator")

def calculator():
    
    numberOne = int(input("Your first number: ")) 

    for symbol in operations:
           print(symbol)
    

    shouldContinue = True

    while shouldContinue:
        
        operationSymbol = input("choose an operation: ")
        numberTwo = int(input("the next number: "))

        calculationFunction = operations[operationSymbol]
        
        answer = calculationFunction(numberOne, numberTwo)
        
        

        print(f"The answer to {numberOne} {operationSymbol} {numberTwo} = {answer}" )
        
        if input(f"Type 'y' to continue calculating with {answer}: or type 'n' to start a new calculation") == "y":
            numberOne = answer
        else:
            shouldContinue = False
            calculator()
            

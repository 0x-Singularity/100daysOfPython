import random

randomNumber = random.randrange(1,100)

hardGuessAmount = 5
easyGuessAmount = 10




print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
userDifficultyChoice = input("Choose a difficulty. Type 'easy' or 'hard':")

if userDifficultyChoice == "easy":
    amountOfUserLives = 10
elif userDifficultyChoice =="hard":
    amountOfUserLives = 5
    
print(f"You have {amountOfUserLives} remaining to guess the number.")


while amountOfUserLives != 0:
    userGuess = int(input("Make a guess: "))
    if(userGuess > randomNumber):
        print("Too high")
        amountOfUserLives = amountOfUserLives - 1
    elif(userGuess < randomNumber):
        print("Too low")
        amountOfUserLives = amountOfUserLives - 1
    elif (userGuess == randomNumber):
        print("You win!")
        print(f"You had {amountOfUserLives} lives remaining")
        quit()
    
print("oops, you ran out of lives.. better luck next time.")


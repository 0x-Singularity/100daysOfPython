import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator\n")
letterChoice = int(input("How many letters would you like in your password?\n"))

symbolChoice = int(input("How many symbols would you like?\n"))

numberChoice = int(input("How many numbers would you like?\n"))

finalPassword =[]

for letterChosen in range (letterChoice):
    random_index = random.randint(0,len(letters)-1)
    finalPassword += (letters[random_index])

for symbolChosen in range (symbolChoice):
    random_index = random.randint(0,len(symbols)-1)
    finalPassword += (symbols[random_index])

for numberChosen in range (numberChoice):
    random_index = random.randint(0,len(numbers)-1)
    finalPassword += (numbers[random_index])

random.shuffle(finalPassword)

password = ""
for character in finalPassword:
    password += character
    
print("Your password is " + password)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']     

def caesar(startText, shiftAmount, cipherDirection):    
    endText = ""    
    if cipherDirection == "decode":
            shiftAmount *= -1 
    for letter in startText:
        position = alphabet.index(letter)         
        newPosition = position + shiftAmount    
        endText += alphabet[newPosition]    
    print(f"the {cipherDirection} text is {endText}")
        
    

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or q to quit:\n")            
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(startText=text, shiftAmount=shift, cipherDirection=direction)






    
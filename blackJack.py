import random
import art

def addCardsToDeck(deckBeingAddedTo,numberOfCardsToBeAdded):
            for i in range (numberOfCardsToBeAdded):
                deckBeingAddedTo.append(random.choice(cards))
                    
def sumOfCards(cardsInDeck):
            return sum(cardsInDeck)
                    

cards = [11, 2, 3, 4 ,5, 6, 7, 8, 9, 10, 10, 10, 10]

usersCards = []
computersCards = []

def blackJack():
    ChoiceToPlay = True
    if(input("Would you like to play BlackJack? reply with a 'y' or 'n': ")) == 'y':
        ChoiceToPlay = True
    else:
        ChoiceToPlay = False
        quit()   
        

        
    while ChoiceToPlay:
        print(art.logo) 

        addCardsToDeck(usersCards,2)
        addCardsToDeck(computersCards,2)
            
        print("Your cards: " + str(usersCards) + ", current score: " + str(sumOfCards(usersCards)))
        print("Computer's first card: " + str(computersCards[0]))
        decisionToContinue = input("type 'y' to get another card, type 'n' to pass:")

        if(decisionToContinue) == 'y':
            addCardsToDeck(usersCards,1)
            print("Your cards: " + str(usersCards) + ", current score: " + str(sumOfCards(usersCards)))
            print("Computer's final hand: " + str(computersCards) + ", final score: " + str(sumOfCards(computersCards)))
            if (sumOfCards(usersCards) > 22):
                print("oops, you went over the limit of 21. You lose")
                blackJack()
            elif (sumOfCards(usersCards) > sumOfCards(computersCards)):
                print("Congrats, you win!")
                blackJack()
            elif((sumOfCards(usersCards) == sumOfCards(computersCards))):   
                print("It's a draw!") 
                blackJack()
            else:
                print("oops, the computer beat you.")   
                blackJack()
                
        elif (decisionToContinue) == 'n': 
            print("your final hand: " + str(usersCards) + ", final score: " + str(sumOfCards(usersCards)))
            print("Computer's final hand: " + str(computersCards) + ", final score: " + str(sumOfCards(computersCards)))
            if (sumOfCards(usersCards) > sumOfCards(computersCards)):
                print("Congrats, you win!")
                blackJack()
            elif((sumOfCards(usersCards) == sumOfCards(computersCards))):   
                print("It's a draw!") 
                blackJack()
            else:
                print("oops, the computer beat you.")
                blackJack()
            
blackJack()
        
    
    


    






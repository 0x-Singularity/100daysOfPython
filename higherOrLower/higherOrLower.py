import random
from art_HOL import logo
from art_HOL import vs
from game_data import data


def formatData(account):
    '''Takes the account data and returns the printable format'''
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    '''Take the user guess and follower counts and returns if they got it right'''
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
    
account_b = random.choice(data)

print(logo)

score = 0

game_should_continue = True

while game_should_continue:

    account_a = account_b 
    account_b = random.choice(data)


    #if the accounts chosen are the same, this will choose another random entry
    while account_a == account_b:
        account_b = random.choice(data)
        
    
    print(f"Your current score is {score}")
    print(f"Compare A: {formatData(account_a)}")

    print(vs)

    print(f"Against B: {formatData(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]


    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right, current score is {score}.")
    else:
        game_should_continue = False
        print(f"You're wrong. Final score {score}")











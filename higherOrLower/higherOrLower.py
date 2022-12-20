import random
from art_HOL import logo
from art_HOL import vs
from game_data import data

print(logo)

account_a = random.choice(data) 
account_b = random.choice(data)


#if the accounts chosen are the same, this will choose another random entry
if account_a == account_b:
    account_b = random.choice(data)
    
    
accountA_name = account_a["name"]
accountA_description = account_a["description"]
accountA_country = account_a["country"]

print(f"{accountA_name}, a {accountA_description}, from {accountA_country}")











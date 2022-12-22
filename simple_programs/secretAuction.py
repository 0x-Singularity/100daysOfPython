bids = {}

biddingFinished = False

def findHighestBidder(biddingRecord):
    highestBid = 0
    for bid in biddingRecord:
        bidAmount = biddingRecord[bid]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bid
    print(f"The winner is {winner} and they won with the price of ${highestBid}")
        

while not biddingFinished:
    name = input("What is your name?")
    price = int(input("What is your price? $"))

    bids[name] = price
    
    shouldContinue = input("Are there any other bidders? Type 'yes' or 'no':")
    if shouldContinue == "no":
        biddingFinished = True
        findHighestBidder(bids)
    



        
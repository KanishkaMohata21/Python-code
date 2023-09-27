import os
bids={}
binding_is_finished=False

def find_highest_bidder(bidding_record):
    highest_amount=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_amount:
            highest_amount=bid_amount
            winner=bidder
    print(f"The winner is {winner} with the bid of {highest_amount}")


while binding_is_finished==False:
    name=input("What is your name?\n")
    price=int(input("What is your bidding price?\n"))
    bids[name]=price
    should_continue=input("Are there any other bidders?YES or NO\n")
    lwr=(should_continue).lower()
    if lwr=="yes":
        os.system("cls")
    else:
        binding_is_finished=True
        find_highest_bidder(bids)


         
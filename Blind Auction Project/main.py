# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)
print("\nWelcome to the Secret Auction Program!!")

more_bidders=True
bidding_data={}

while more_bidders!=False:
    inp_name = input("What is your name? : ")
    inp_bid = int(input("What's your bid? : $"))
    bidding_data[inp_name]=inp_bid
    check_bidders= input("Are there more bidders? Type 'yes' or 'no'.\n")
    if check_bidders == "yes":
        print("\n"*100)
    else:
        more_bidders=False

highest_bid=0
winner=""
for key in bidding_data:
    bid_amount=bidding_data[key]
    if bid_amount>highest_bid:
        highest_bid=bid_amount
        winner=key

print("\n"*100)
print(f"The winner is {winner} with a bid of ${highest_bid}")

#Also google code to clear output screen more easily


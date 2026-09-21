from art import logo
print(logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
def highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids = {}
biddding = True
while biddding:
    name = input("What is your name? ")
    bid_amount = float(input("What is your bid? $"))
    bids[name] = bid_amount
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if other_bidders == "no":
        bidding = False
        highest_bidder(bids)

    elif other_bidders == "yes":
        print("\n" * 100)




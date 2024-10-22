import art


print(art.auction_logo)

bidders = {}
loop = True

while loop:
    name = input("Welcome to the auction, if you are interested in bidding write your name: ")
    bid = input("How much would you like to bid?: €")

    bidders[name] = float(bid)

    keep_loop = input("Is there another bidder? (yes/no): ").lower()

    if keep_loop == "yes":
        loop = True
    elif keep_loop == "no":
        loop = False
    else:
        print("huh?")


highest_bidder = max(bidders, key=bidders.get)  # Get the name of the highest bidder
highest_bid = bidders[highest_bidder]  # Get the highest bid amount

# Print the results
print(f"The highest bid is €{highest_bid} by {highest_bidder}.")

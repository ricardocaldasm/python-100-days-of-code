from replit import clear

participant = dict()


def highest_bid(record):
    max_bid = 0
    winner = ""
    for bidder in record:  # bidder = key
        if record[bidder] > max_bid:
            max_bid = record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${max_bid}")


while True:
    name = str(input("What is your name? "))
    participant[name] = float(input("What is your bid? $"))
    flag = (
        str(input("Are there any other bidders? Type 'yes or 'no': ")).lower().strip()
    )
    while flag != "yes" and flag != "no":
        flag = str(input("Please type 'yes' or 'no': ")).lower().strip()
    if flag == "yes":
        clear()
    elif flag == "no":
        highest_bid(participant)
        break

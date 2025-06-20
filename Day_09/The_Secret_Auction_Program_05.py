logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
                        
'''
print(logo)

bids = {}
bidding_finished = True


def find_highest_number(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while bidding_finished:
  name = input("What is your name? ")
  price = int(input("what is your bid? $ "))
  bids[name] = price # name = key, price = value
  should_continue = input("Are there any other bidders ? 'yes' or 'no' ")
  if should_continue == "no":
    bidding_finished = False
    find_highest_number(bids)
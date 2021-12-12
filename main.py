from replit import clear
import art

print(art.logo)

def calculate_winner(bids_dict):
  '''Iterates over dictionary to find the highest bid. Returns winner and their bid.'''
  winner = ''
  winning_bid = 0
  for key, value in bids_dict.items():
    if value > winning_bid:
      winning_bid = value
      winner = key
  print(f"The winner is {winner} with a bid of ${winning_bid}")

more_bids = True
all_bids = {}

while more_bids:
  name = input("Bidder name:\n")
  bid = float(input("Bid amount: \n$"))
  repeat = input("Are there more bidders? Enter 'y' or 'n': \n")

  all_bids[name] = bid
  if repeat.lower() == 'n':
    more_bids = False
    calculate_winner(all_bids)
  else:
    clear()

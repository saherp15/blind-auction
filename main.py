from replit import clear
from art import logo
print(logo)
bids={}
bidding_finishes=False
#bidding_records  is dictionary of all bidding
def highest_bidder(bidding_records):
  highes_bid=0
  winner=""
  for bidder in bidding_records:
    bid_amt=bidding_records[bidder]
    if bid_amt>highes_bid:
      highes_bid=bid_amt
      winner=bidder
  print(f"The winner is {winner} with a bid of ${highes_bid}")
      
    
    
  
while not bidding_finishes:
  name=input("What is your name?: ")
  price=int(input("What is your bid?: $"))
  bids[name]=price
  new_input=input("Are there any other bidder? Type 'Yes' or 'No'. ").lower()
  if new_input=="no":
    bidding_finishes=True
    highest_bidder(bids)
  elif new_input=="yes":
    clear()
    



from overlap import overlap
from remove import remove

def transfer(recipient, outcome, funding, amount):
  if overlap(recipient, outcome, funding) >= amount:
    funding = funding - amount
    outcome = remove(outcome, recipient, amount)
  else:
    amount = 0

  return (amount, outcome, funding)

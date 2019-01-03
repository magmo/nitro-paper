from overlap import overlap
from remove import remove
from cap import cap

MAX = 2**256

def claim(recipient, guarantee, outcome, funding, amount):
  cappedGuarantee = cap(guarantee, outcome)
  if overlap(recipient, cappedGuarantee, funding) >= amount:
    funding = funding - amount
    guarantee = remove(cappedGuarantee, recipient, amount)
    outcome = remove(outcome, recipient, amount)
  else:
    amount = 0

  return (amount, guarantee, outcome, funding)

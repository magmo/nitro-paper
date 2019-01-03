from overlap import overlap
from remove import remove
from restrict import restrict

MAX = 2**256

def claim(recipient, guarantee, outcome, funding, amount):
  potentialPayout = overlap(recipient, outcome, MAX)
  # todo: need to 'fully restrict' the guarantee
  restrictedGuarantee = restrict(guarantee, recipient, potentialPayout)
  if overlap(recipient, restrictedGuarantee, funding) >= amount:
    funding = funding - amount
    guarantee = remove(restrictedGuarantee, recipient, amount)
    outcome = remove(outcome, recipient, amount)
  else:
    amount = 0

  return (amount, guarantee, outcome, funding)

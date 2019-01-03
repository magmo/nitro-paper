def restrict(outcome, recipient, amount):
  newOutcome = []
  for [address, allocation] in outcome:
    if address == recipient:
      newAllocation = min(allocation, amount)
      amount = amount - newAllocation
      newOutcome.append([address, newAllocation])
    else:
      newOutcome.append([address, allocation])

  return newOutcome

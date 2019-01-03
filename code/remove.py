def remove(outcome, recipient, amount):
  newOutcome = []
  for [address, allocation] in outcome:
    if address == recipient:
      reduction = min(allocation, amount)
      amount = amount - reduction
      newOutcome.append([address, allocation - reduction])
    else:
      newOutcome.append([address, allocation])

  return newOutcome

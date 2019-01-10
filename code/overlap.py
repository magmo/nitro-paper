def overlap(recipient, outcome, funding):
  for [address, allocation] in outcome:
    if funding <= 0:
      return 0;
    elif address == recipient:
      return min(allocation, funding)
    else:
      funding -= allocation

  return 0

def overlap(recipient, outcome, funding):
  result = 0
  for [address, allocation] in outcome:
    if funding <= 0:
      break;

    if address == recipient:
      result += min(allocation, funding)
    funding -= allocation

  return result

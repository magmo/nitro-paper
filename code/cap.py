from collections import defaultdict

def cap(outcome, outcome2):
  totals = defaultdict(int)
  for [address, allocation] in outcome2:
    totals[address] += allocation

  cappedOutcome = []
  for [address, allocation] in outcome:
    remaining = totals[address]
    newAllocation = min(allocation, remaining)
    cappedOutcome.append([address, newAllocation])
    totals[address] -= newAllocation
  
  return cappedOutcome

interface Holdings { [address: string]: number; }
interface Allocations { [address: string]: Allocation; }
type Allocation = { address: string; amount: number; }[];

class TurboAdjudicator {
  holdings: Holdings;
  allocations: Allocations;

  constructor() {
    this.holdings = {};
    this.allocations = {};
  }

  register(address: string, allocation: Allocation): boolean {
    if (this.allocations[address]) { return false; }

    this.allocations[address] = allocation;
  }

  transfer(fromAddress: string, toAddress: string, amount: number): boolean {
    if (!this.holdings[fromAddress]) { return false; }
    let fundsAvailable = this.holdings[fromAddress];

    if (!this.allocations[fromAddress]) { return false; }
    const allocation = this.allocations[fromAddress];

    allocation.forEach((item) => {
      if (fundsAvailable < amount) { return false; }
      if (item.address == toAddress) {
        if (item.amount >= amount) {
          this.holdings[fromAddress] -= amount;
          this.holdings[toAddress] += amount;
          item.amount -= amount;
        } else {
          return false;
        }
      }
      fundsAvailable -= item.amount;
    });

    return false;
  }
}

class TurboAdjudicator
  def initialize
    @holdings = Hash.new(0)
    @allocations = Hash.new(nil)
  end

  def register(allocation, channelAddress)
    @allocations[channelAddress] ||= allocation
  end

  def transfer(fromAddress, toAddress, amount)
    if canAfford?(fromAddress, toAddress, amount)
      @holdings[fromAddress] += amount
      @holdings[toAddress] -= amount
      @allocations[fromAddress].each do |entry|
        if addr = toAddress
      end
    end
  end

  def canAfford?(fromAddress, toAddress, amount)
    fundsAvailable = @holdings[fromAddress]
    return false if fundsAvailable < amount

    allocation = @allocations[fromAddress]
    return false if allocation.nil?

    allocation.each do |address, total|
      return true if address == toAddress && amount <= total

      fundsAvailable -= total
    end

    return false
  end
end

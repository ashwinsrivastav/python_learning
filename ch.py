def stock(prices):
    a=[]
    if sorted(prices,reverse=True)==prices:
        return 0
    if (prices.index(min(prices)))<(prices.index(max(prices))):
        return max(prices)-min(prices)
    for count in range(len(prices)):
        for i in range(prices.index(max(prices))):
            a.append(max(prices)-prices[i])
        prices.remove(max(prices))
    return max(a)
prices=[11,7,4,1,2]
print(stock(prices))
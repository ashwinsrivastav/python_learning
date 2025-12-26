def getDescentPeriods(prices):
    tot=len(prices)
    if len(prices)==1:
        return tot
    for i in range(len(prices)-1):
        j=i+1;a=1
        if prices[i]-prices[j]==a:
            while prices[i]-prices[j]==a:
                j+=1
                a+=1
                if j==len(prices):
                    break
            tot+=1
    return tot
p=[3,2,1,4]
print(getDescentPeriods(p))
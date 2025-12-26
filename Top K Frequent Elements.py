def ch(nums,k):
    freq={};ret=[];count=1
    for i in nums:
        freq[i] = freq.get(i, 0) + 1
    c=sorted(list(freq.values()))
    while True:
        for key,value in freq.items():
            if value==c[-count]:
                ret.append(key)
                count+=1
            if count==k+1:
                return ret
        count=len(ret)+1
        if count==k+1:
            return ret
nums =[5,3,1,1,1,3,73,1]; k = 2
print(ch(nums,k))

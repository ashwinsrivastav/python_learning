nums = [4,3,2,7,8,2,3,1]
m=[]
for i,j in zip((range(1,len(nums)+1)),(range(len(nums),-1))):
    print(i,j)
    if i!=j:
        if i not in nums:
            m.append(i)
        if j not in nums:
            m.append(j)
print(m)
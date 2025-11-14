nums=[0,0,1,1]
a=[];count=0
for i in nums:
    if nums.count(i)>1:
        a.append(i)
        nums.remove(i)
        count+=1
        if count==2:
            print(a)
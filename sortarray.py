from numpy import *
nums=array([0,0,1,1,1,2,2,3,3,4]);new=[];a=0
for i in nums:
    if i in nums:
        if i not in new:
            new.append(i)
myarray=array(new)
print(myarray)

from array import *
def odd(nums):  
    nums=sorted(nums)
    print(nums)
    for i in nums:
        nums.remove(i)
        print(nums)
        if i not in nums:
            return i
def dec():
    dic={}
nums=array('i',[1,0,1,0,7,9,7])
print(len(nums))
#print(sorted(nums))
print(odd(nums))
print(nums)
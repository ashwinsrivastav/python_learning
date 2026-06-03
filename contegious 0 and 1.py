def check(nums): #too many errors 
    o=0;l=0;i=0;max=0;temp=0
    while i<len(nums):
        if nums[i]==0:
            while i<len(nums) and nums[i]==0:
                o+=1
                i+=1
                temp=o
            while i<len(nums) and nums[i]==1 and temp>0:
                l+=1
                i+=1
                temp-=1
            if temp==0:
                if o*2>max:
                    max=o*2
            else:
                if l*2>max:
                    max=l*2
            l,o=0,0
        else:
            while i<len(nums) and nums[i]==1:
                l+=1
                i+=1
                temp=l
            while i<len(nums) and nums[i]==0 and temp>0:
                o+=1
                i+=1
                temp-=1
            if temp==0:
                if l*2>max:
                    max=l*2
            else:
                if o*2>max:
                    max=o*2
            l,o=0,0
    return max
nums=[0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0]
print(check(nums))

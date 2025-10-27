nums=[1,0,4,3];j=0
for i in sorted(nums):
    if i!=j:
        print(j)
    elif i==j:
        j+=1
nums=[0,0,1]
count=0
for i in sorted(nums, reverse=True):
    if i==0:
        nums.remove(i)
        count+=1
for i in range(count):
    nums.append(0)
print(nums)
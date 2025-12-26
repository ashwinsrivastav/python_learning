left = 1; right = 22
lis=[]
for i in range(left,right+1):
    temp=i
    if i<10:
        lis.append(i)
    else:
        while temp>0:
            a=temp%10
            if a==0:
                break
            if i%a==0:
                pass
            else:
                break
            temp=temp//10
            if temp==0:
                lis.append(i)
print(lis)
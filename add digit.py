num=38
sum=0
while num%10!=num:
    while num>0:
        sum=sum+num%10
        num=int(num/10)
    num=sum
    sum=0
print(num)
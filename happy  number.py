def isHappy(n: int) -> bool:
    count=0
    for i in range(200):
        a=0
        while n>0:
            a=a+(n%10)**2
            n=n//10
            count+=1
        if a==1:
            return True
        elif count<100:
            n=a
            continue
        else:
            return False
n=int(input("enter a number"))
print(isHappy(n))

       

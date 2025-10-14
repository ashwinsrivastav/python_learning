def prime(n):
    b=n//2
    for i in range(2,b):
        if n%i==0:
            return False
    else:
        return True
a=int(input("enter the number till you want the series"))
if a<2:
    print("invalid input")
else:
    for i in range(2,a):
        if prime(i):
            print(i,end=",")
            #checking shit
 

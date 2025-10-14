from numpy import *
num=array([3,3,9,8,7,5,3,0,9])
z=int(input("enter the target"))
for i in range(len(num)):
    for j in range(len(num)):
        if num[i]+num[j]==z and i!=j:
             break
    if j!=len(num)-1:
        break
a=array([i,j])
print(a)
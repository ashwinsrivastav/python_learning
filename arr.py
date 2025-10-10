from array import *
x=array('i',[])
for i in range(5):
    y=int(input())
    x.append(y)
print(x)
print("enter the value to search")
val=int(input())
print(x.index(val))
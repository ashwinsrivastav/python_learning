x=input("enter a string-")
y=len(x)
c=0 
a=0
space=" "
for i in range(y):
    if x[i]==space:
         a=i 
if a!=0:
    c=a-y
    x=x[-1:c:-1]
x[-1::-1]
print(x)
print(len(x))


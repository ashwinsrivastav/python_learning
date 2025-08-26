def cal():
    if c=="+":
     return(a+b)
    elif c=="-":
     return(a-b)
    elif c=="*":
     return(a*b)
    elif c=="/":
     return(a/b)
    else:
     print("wrong input")
     return "a"
print("calculator")
a=eval(input("enter the first number"))
b=eval(input("enter the second number"))
c=input("enter the operation")
result=cal()
if result!="a":
 print(result)

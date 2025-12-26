operations=["5","-2","4","C","D","9","+","+"]
a=[]
for i in operations:
    if i[0]=='-':
        a.append(int(i))
    elif i.isnumeric():
        a.append(int(i))
    elif i=="+":
        a.append(a[-1]+a[-2])
    elif i=="D":
        a.append(2*a[-1])
    else:
        a.pop()
print(sum(a))
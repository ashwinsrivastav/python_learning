num=5
a=bin(num)[2:];b=''
print(a)
for i in a:
    if i=='0':
        b=b+'1'
    else:
        b=b+"0"
print(int(b,2))
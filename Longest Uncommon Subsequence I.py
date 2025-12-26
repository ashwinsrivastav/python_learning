a = "aaa"; b = "aaa"
c='';x=[]
for i,j in zip(a,b):
    if i!=j:
        c=c+i
        continue
    x.append(len(c))
    c=''
x.append(len(c))
if max(x)==0:
    print('-1')
else:
    print(max(x))


list1 = ["happy","sad","good"]; list2 = ["sad","happy","good"]
a=[];b=[];c=[]
for i in list1:
    if i in list2:
        a.append(list1.index(i)+list2.index(i))
        b.append(i)
print(a,b)
for i in range(len(a)):
    if a[i]==min(a):
        c.append(b[i])
print(b[a.index(min(a))])
print(c)
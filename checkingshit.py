a=[1,2,3] #list
b={1,2,3} #set
c=(2,4,3) #tuple
d={'car':4,'bike':2} #dictionary
d['bike']=55
print(a)
print(b)
print(c)
e=a[2]
a[1]=e
print(e)
print(a[1])
print(d['bike'])
print(c[1]+3)
a[1]=c[1]+3
print(a)

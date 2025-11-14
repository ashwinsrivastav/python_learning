s = ["h","e","l","l","o"]
"""for i in range(len(s)//2):
    temp=s[i]
    s[i]=s[-i]
    s[-1]=temp
print(s)"""
a=s[::-1];s=[]
print(a)
for i in range(len(a)):
    s.append(a[i])
print(s)
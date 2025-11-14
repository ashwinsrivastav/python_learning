def aah(s,t):  
    count=0
    for i in s:
        if i in t:
            count+=1
            a=t.index(i)
            t=t[a+1:]
    if count==len(s):return True
    return False

s = "aaaaaa"
t ="bbaaaa"
print(aah(s,t))
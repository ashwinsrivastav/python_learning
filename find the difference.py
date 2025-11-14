def ch(s,t):
    a=len(t) 
    for i in s:
        t=t.replace(i,"")
        a-=1
        if a==len(t):
            continue
        else:
            t=t+i
    return t
s = "a"
t = "aa"
print(ch(s,t))
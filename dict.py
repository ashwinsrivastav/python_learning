def check(dic,s):
    if len(pattern)!=len(s):
        return False
    for val,i in zip(range(len(s))):
        if dic[val]!=s[i]:
            return False
    else:
        return True
pattern="jquery"; s = "jquery"
s=s.split()
dic=dict(zip(pattern,s))
print(check(dic,s))

        
s="abcdefghij";k=2
rev="";count=0;valid=0;res=""
for i in range(len(s)):
    if valid==0:
        rev+=s[i]
        count+=1
        if count==k:
            valid=1
            count=0
            res+=rev[::-1]
            rev=""
    else:
        rev+=s[i]
        count+=1
        if count==k:
            valid=0
            count=0
            res+=rev
            rev=""
if valid==0:
    res+=rev[::-1]
else:
    res+=rev
print(res)
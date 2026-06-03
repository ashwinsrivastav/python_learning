s = "aaababc" 
res = "" 
count = 1 
for i in range(len(s)-1): 
    if s[i] == s[i+1]: 
        count += 1 
    else: 
        res += s[i] + str(count) 
        count = 1 
res += s[-1] + str(count) 
print(res)
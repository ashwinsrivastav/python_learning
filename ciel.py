def evaluate(s,knowledge):
    pair={};res=""
    for i in knowledge:
        pair[i[0]]=i[1]
    i=0
    while i<len(s):
        if s[i]=="(":
            key=""
            start=i
            while s[i+1]!=")":
                key+=s[i+1]
                i+=1
            end=i+1
            if key in pair.keys():
                s=s[:start]+pair[key]+s[end+1:]
            else:
                s=s[:start]+"?"+s[end+1:]
            i=start
        else:
            i+=1
    return s
print(evaluate("(name)(name)is(age)yearsold",[["name","bob"],["age","two"]]))
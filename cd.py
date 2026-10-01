def maximumLengthSubstring(s):
    dic={}
    i=0;max=[];substr=[]
    while i<len(s):
        dic[s[i]]=dic.get(s[i],0)+1
        substr.append(s[i])
        if dic[s[i]]>2:
            dic.clear()
            max.append(len(substr))
            substr=substr[substr.index(s[i])+1:]
            print(substr)
            for j in substr:
                dic[j]=dic.get(j,0)+1
        i+=1
    max.append(len(substr))
    print(max)
s="bcbbbcba"
maximumLengthSubstring(s)
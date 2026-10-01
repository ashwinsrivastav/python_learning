def smallestSubsequence(s):
    leng=len(set(s))
    for i in range(len(s)-leng+1):
        sub=s[i:leng+i]
        for j in range(len(sub)-1):
            if ord(sub[j])<ord(sub[j+1]):
                pass
            else:
                break
        else:
            return sub
print(smallestSubsequence("cbacdcbc"))
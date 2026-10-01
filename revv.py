def reverseParentheses(s):
    n=len(s);res=""
    def recursive_bitch(i,s,n):
        stack=[];paranthesis=[]
        while i<n and s[i]!=")" and s[i]!="(":
            stack.append(s[i])
            i+=1
        if s[i]=="(":
            paranthesis.append("(")
            temp,i=recursive_bitch(i+1,s,n)
            stack.extend(temp)
        elif s[i]==")":
            paranthesis.pop()
            stack.reverse()
        if paranthesis:
            return stack,i
        else:
            temp,i=recursive_bitch(i,s,n)
            stack.extend(temp)
        
    i=0
    while i<n:
        if s[i]=="(":
            stack,i=recursive_bitch(i,s,n)
            res=res+"".join(stack)
        elif s[i]==")":
            i+=1
        else:
            res+=s[i]
            i+=1
    return res
print(reverseParentheses("(u(love)i)"))

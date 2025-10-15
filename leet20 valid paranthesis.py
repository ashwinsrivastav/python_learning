#to check if the paranthesis is in right order on not
s="(){}"
def pren():
    stack=[]
    for i in range(len(s)):
        try:
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                stack.append(s[i])
            elif (s[i]==")" and stack[-1]=="(") or (s[i]=="}" and stack[-1]=="{") or (s[i]=="]" and stack[-1]=="["):
                stack.pop()
            else:
                break
        except IndexError:
            return False
            break
    if len(stack)==0:
        return True
    else:
        return False
print(pren())
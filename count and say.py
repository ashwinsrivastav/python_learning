def countAndSay(n: int) -> str:
    if n==1:
        return "1"
    def recursive_shit(n,string,x):
        if x==n-1:
            return string
        x+=1
        count=0;res=""
        for i in range(len(string)-1):
            if string[i]==string[i+1]:
                count+=1
            else:
                res+= str(count+1)+string[i]
                count=0
        res+=str(count+1)+string[-1]
        return recursive_shit(n,res,x)
    return recursive_shit(n,"11",1) 
print(countAndSay(n=5))
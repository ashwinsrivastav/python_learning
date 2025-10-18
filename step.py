def stair(x: int) -> int:
    if x<=1:
        return x
    return stair(x-1)+stair(x-2)
n = int(input("enter the steps: "))
print(stair(n+1))

'''
prev=0; curr=1
        for i in range(n):
            curr=prev+curr
            prev=curr-prev
     return curr
     
    '''

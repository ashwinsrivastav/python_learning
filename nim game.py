import math
def nim(): 
    if n<4:
        return True
    elif (math.ceil(n/3))%2==0:
        return False
    else:
        return True
n=8
print(nim())
print(math.ceil(n/3)%2)
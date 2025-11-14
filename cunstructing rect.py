import math
def rec(area):
    a=int(math.sqrt(area));w=a
    for l in range(a,area):
        for w in range(a,1,-1):
            if l*w==area:
                return [l,w]
            elif l*w<area:
                break
    else:
        return [area,1]
area=999994
print(rec(area))
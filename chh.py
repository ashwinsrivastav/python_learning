points =[[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]];i=0
points=sorted(points);arrow=len(points)
while i<len(points)-1:
    if points[i][1]>=points[i+1][0]:
        arrow-=1
        i+=1
    i+=1
print(arrow)
print(points)
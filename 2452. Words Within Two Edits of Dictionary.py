queries =["tsl","sri","yyy","rbc","dda","qus","hyb","ilu","ahd"]
dictionary = ["uyj","bug","dba","xbe","blu","wuo","tsf","tga"]
error=0;res=[]
for i in queries:
    for j in dictionary:
        for x in range(len(j)):
            if i[x]!=j[x]:
                error+=1
        if error>2:
            pass
        else:
            res.append(i)
            error=0
            break
        error=0
print(res)
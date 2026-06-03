s="abcd"
indices=[0, 2]
sources=["a", "cd"]
targets=["eee", "ffff"]
res=s
for i in range(len(indices)):
    lenght=len(sources[i])
    if sources[i]==s[indices[i]:indices[i]+lenght]:
        res=res.replace(sources[i],targets[i])
print(res)

inp="dog cat apple dog banana cat"
val=inp.split()
uni=sorted(set(val));print(uni)
dic={}
for i,j in zip(uni,range(len(uni))):
    dic[i]=j
print(" ".join([str(dic[x]) for x in val]))

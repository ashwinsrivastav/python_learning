#def unique():
    #for i in range(len(s)):

            
        
s="vvebb"
print(sorted(s))
for i in range(len(s)):
    sorted(s).remove(s[i])
    if s[i] not in s:
        print(s.index(i))

#print(unique())
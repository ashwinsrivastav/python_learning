'''for i in range(1,101):
    if (i%3==0 or i%5==0):
        continue
    else:
        print(i,end=' ')'''

for i in range(2,101):
    a=0
    for j in range(2,i/2):
        if i%j==0:
            a=1
            break
    if a==0:
        print(i,"is prime")
        
         
          
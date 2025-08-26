a=int(input('enter a number'))
upper_space=a
lower_space=1
for i in range(0,a+1):
    for b in range(i):
        print('*',end='')
    for b in range(upper_space,0,-1):
        print(' ',end='')
    for b in range(upper_space,0,-1):
        print(' ',end='')
    upper_space-=1
    for b in range(i,0,-1):
        print('*',end='')
    print()
for i in range(a-1,0,-1):
    for b in range(i):
        print('*',end='')
    for b in range(lower_space):
        print(' ',end='')
    for b in range(lower_space):
        print(' ',end='')
    lower_space+=1
    for b in range(i,0,-1):
        print('*',end='')
    print()
a=input("enter your full name:-")
first_intial=a[0]
print("your initials are:-",end="")
print(first_intial,end=" ")
lenght= len(a)
i=0
#print(lenght)
second_intial=0
space_finder=" "
while  i<lenght:
    if space_finder==a[i]:
       second_intial=i+1
       print(a[second_intial],end=" ")
    i+=1

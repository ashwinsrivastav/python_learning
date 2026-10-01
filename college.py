def college(name,roll_number,option):
    print(F"your name is {name} and your roll number {roll_number}")
    if option=="A":
        print("your marks are 500 out 700")
    elif option=="B":
        print("you have no fees due")
    elif option=="C":
        print("You have 0 backs at present")
    else:
        print("invalid input")
    print("")
print("Enter you name- ")
name=input()
roll_number=int(input("enter your 3 digit roll number- "))
print("what would you like to know")
print("A: last result")
print("B: fees due")
print("C: number of backs")
option=input("Enter your choice- ")
college(name,roll_number,option)

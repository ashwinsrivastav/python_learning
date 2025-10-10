import random
a=0;guess_count=0
def check():
    if user_input==ran_num:
        return True
    else:
        return False
print("it's a game of guess, the program has chosen a number between 1 to 100 and you have to guess it!")
ran_num=random.randint(1,100)
#print(ran_num)
print("enter your guess")
while a<1:
    user_input=int(input())
    guess_count+=1
    if check():
        print(f"wow!,you've won in {guess_count} attempts")
        game_over=1
    else:
        if (user_input>ran_num):
            print("Entered number is greater,Try again!")
        else:
            print('Entered number is smaller,Try again!')
print("the end")

    
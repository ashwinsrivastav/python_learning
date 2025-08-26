def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = check_odd_even(num)
    print(num,"is",result)
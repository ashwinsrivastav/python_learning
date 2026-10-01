sign=["+","*","/","-","%"]

print("-----CALCULATOR------")
print("Enter the fucnton you want to calculate with proper spacing- ")
print("for example - 76 + 78")
print("operator available ",sign)


function=input()
function=list(function.split())
number1= float(function[0])
number2= float(function[2])


if function[1] in sign and len(function)==3:
    if function[1]=="+":
        result= number1+number2
        print(F"the result ={result}")
    elif function[1]=="-":
        result= number1-number2
        print(F"the result ={result}")
    elif function[1]=="*":
        result= number1*number2
        print(F"the result ={result}")
    elif function[1]=="/":
        if number2!=0:
            result= number1/number2
            print(F"the result ={result}")
        else:
            print("Invalid input")
    elif function[1]=="%":
        result= number1%number2
        print(F"the result is ={result}")
    print("program complete")
else:
    print("Invalid operator")






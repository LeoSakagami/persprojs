
def Main():
    Input=input("Calculator booted, what would you like to do\n")
    Numbers = Input.split()
    FirstNumber=int(Numbers[0]) 
    SecondNumber=0  
    if len(Numbers)==3:
        SecondNumber=int(Numbers[2])
    if Input.find("+")>-1:
        print(addition(FirstNumber,SecondNumber))
    elif Input.find("-")>-1:
        print(subtraction(FirstNumber,SecondNumber))
    elif Input.find("/")>-1:
        print(divide(FirstNumber,SecondNumber))
    elif Input.find("x")>-1:
        print(multiply(FirstNumber,SecondNumber))
    elif Input.find("!")>-1:
        print(factorio(FirstNumber))

def addition(num1, num2):
    return num1+num2

def subtraction(num1, num2):
    return num1-num2

def divide(num1, num2):
    return num1/num2

def multiply(num1,num2):
    return num1*num2

def factorio(num1):
    if num1<=1:
        return 1
    return num1*factorio(num1-1)
 
Main()
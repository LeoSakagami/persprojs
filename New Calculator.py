def addition(num1,num2):
    return num1+num2 

def subtraction(num1,num2):
    return num1-num2

def division(num1,num2):
    return num1/num2

def multiplication(num1,num2):
    return num1*num2
    
def main():
    Input=input("Calculator2 booted, what would you like to do\n")
    Numbers = Input.split()

    while len(Numbers)>2:

        FirstNumber = int(Numbers[0]) #print(type(FirstNumber))  # prints type int
        SecondNumber = int(Numbers[2])     

        if Numbers[1]=='+':
            Numbers[0]=addition(FirstNumber,SecondNumber)
        
        if Numbers[1]=='-':
            Numbers[0]=subtraction(FirstNumber,SecondNumber)

        if Numbers[1]=='/':
            Numbers[0]=division(FirstNumber,SecondNumber)

        if Numbers[1]=='*':
            Numbers[0]=multiplication(FirstNumber,SecondNumber)
        del Numbers[1]
        del Numbers[1]
    print(Numbers[0])
#print(Numbers)# FIRST NUMBER TURNS INTO THIS EX: [1, '+', 2] ----> [3, '+', 2]
main()
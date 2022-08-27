from art import logo

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1-num2

def divide(num1, num2):
    return num1/num2

def multiply(num1, num2):
    return num1*num2

operation={"+":add,
           "-":subtract,
           "/":divide, 
           "*":multiply}

def calculator():
    print(logo)
    num1= float(input("What's the first number?:"))
    for keys in operation:
        print(keys)
        proceed= "y"

    while (proceed == "y"):
        calculator()
        num2=float(input("What's the second number?:"))


        key_choice=("Pick an operation from the line above:")

        answer=operation[key_choice](num1,num2)

        print(f"{num1} {key_choice} {num2} = {answer}")

        proceed=input(f"Type 'y' to continue calculating with {answer}, or type 'n'  to start a new calculation:")

        if proceed == "n":
            num1=answer

        else:
            proceed="y"

calculator()
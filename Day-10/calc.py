



def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


operations={"+":addition,
            "-":subtraction,
            "*":multiplication,
            "/":division}
def calculator():
    a=int(input("What is the first number?"))
    flag=True
    
    while flag:
        for symbols in operations:
            print(symbols)
        op = input("What is the operation?")
        while op not in operations:
            op=input("Enter a valid operator")
        b = int(input("What is the next number?"))
        ans = operations[op](a, b)
        print(f"{a} {op} {b} is {ans}")
        f=input("Do you want to continue?(y/n) or do you want to start a new calculation (ac)")
        if f=="n":
            flag=False
        elif f=="ac":
            calculator()
        else:
            a=ans


calculator()








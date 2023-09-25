def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operators={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    num1=float(input("What is the first number?"))

    for operator in operators:
        print(operator)

    should_continue=True

    while should_continue==True:    
        operation_symbol=input("Pick a operation:")
        num2=float(input("What is the next number?"))
        calculation_function=operators[operation_symbol]
        answer=calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer},or type 'n' to start again:")=="y":
            num1=answer
        else:
            should_continue=False
            calculator()


calculator()
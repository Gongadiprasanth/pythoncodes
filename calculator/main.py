def addition(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations ={
    "+":addition,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    num1 = int(input("what is the first number"))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        symbol_operation =input("enter the symbol to perform the operation")
        num2 =int(input("what is the next number"))
        calculation_function =operations[symbol_operation]
        answer =calculation_function(num1,num2)
        print(f"{num1}{symbol_operation}{num2}={answer}")
        if input(f"'y' to continue {answer}to exit type 'n' start new calculation") == "y":
            num1 = answer
        else:
            should_continue=False
            calculator()

calculator()


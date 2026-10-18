number1=int(input("Enter your first number : "))
Operator=input("Operator:")
number2=int(input("Enter your secon number : "))
def add (number1,number2):
    sum=number1+number2
    return sum
def subtract (number1,number2):
    Subtract=number1-number2
    return Subtract
def multiply (number1,number2):
    Multiply=number1*number2
    return Multiply
def divide (number1,number2):
    Divide= number1/number2
    return Divide
operations={
    "+":add
    ,"-":subtract
    ,"*":multiply
    ,"/":divide
}

operation_fountion=operations[Operator]
answer=operation_fountion(number1,number2)
print("{} {} {} = {}".format(number1,Operator,number2,answer))

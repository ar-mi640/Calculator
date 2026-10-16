number1=int(input("Enter your first number : "))
Operator=input("Operator:")
number2=int(input("Enter your secon number : "))
if Operator is "+":
    add(number1,number2)
if Operator is "-":
    subtract(number1,number2)
if Operator is "*":
    multiply(number1,number2)
if Operator is "/":
    divide(number1,number2)
def add():
    sum=number1+number2
    return"{}+{}={}".format(number1,number2,sum)
def subtract(number1,number2):
    Subtract=number1-number2
    return f"{number1}-{number2}={Subtract}"
def multiply(number1,number2):
     Multiply=number1*number2
    return "{}*{}={}".format(number1,number2,Multiply)
def divide(number1,number2):
     Divide= number1/number2
    return "{}/{}={}".format(number1,number2,Divide)

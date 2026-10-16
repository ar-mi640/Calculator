operations={
    "+":add
    ,"-":subtract
    ,"*":multiply
    ,"/":divide
}
number1=int(input("Enter your first number : "))
Operator=input("Operator:")
number2=int(input("Enter your secon number : "))
operation_fountion=operation[Operator]
answer=operation_fountion(number1,number2)
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

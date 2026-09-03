number1=int(input("Enter your first number : "))
Operator=input("Operator:")
number2=int(input("Enter your secon number : "))
if Operator is "+":
    sum=number1+number2
    print("{}+{}={}".format(number1,number2,sum))
if Operator is "-":
    Subtract=number1-number2
    print(f"{number1}-{number2}={Subtract}")
if Operator is "*":
    Multiply=number1*number2
    print("{}*{}={}".format(number1,number2,Multiply))
if Operator is "/":
    Divide= number1/number2
    print("{}/{}={}".format(number1,number2,Divide))

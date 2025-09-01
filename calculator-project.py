#import math function because perform mathematical technics
import math

#step-1 creat funtion 

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def divide(num1,num2):
    return num1/num2

def multplay(num1,num2):
    return num1*num2

def module(num1,num2):
    return num1%num2

def sin(num1):
    return math.sin(num1)

def cos(num1):
    return math.cos(num1)

def tan(num1):
    return math.tan(num1)

def squareroot(num1):
    return math.sqrt(num1)

def fact(num1):
    return math.factorial(num1)

def square(num1,num2):
    return math.pow(num1,num2)


#step-3 creat list of opration


print(" pleace select your operation:\n" 
        "1.Addtion\n"
        "2.substration\n"     
        "3.divide\n"
        "4.multiplay\n"
        "5.module\n"
        "6.sin\n"
        "7.cos\n"
        "8.tan\n"
        "9.squareroot\n"
        "10.factoial\n"
        "11.square"
        )
select=int(input("Enter your opperation:\n"))


if select == 1 :
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print("addtion is",num1,"+",num2,"=",add(num1,num2))


elif select == 2 :
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print("subsration is",num1,"-",num2,"=",sub(num1,num2))


elif select == 3 :
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    print("divided is",num1,"/",num2,"=",divide(num1,num2))


elif select == 4 :
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print("multipliction is",num1,"*",num2,"=",multplay(num1,num2))


elif select == 5 :
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print("module is",num1,"%",num2,"=",module(num1,num2))


elif select == 6 :
    num1=int(input("Enter first number:"))
    print("sin value",num1,"is=",sin(num1))


elif select == 7 :
    num1=int(input("Enter first number:"))
    print("cos value",num1,"is=",cos(num1))


elif select == 8 :
    num1=int(input("Enter first number:"))
    print("tan value",num1,"is=",tan(num1))


elif select == 9 :
    num1=int(input("Enter first number:"))
    print("square value",num1,"is=",squareroot(num1))


elif select == 10 :
    num1=int(input("Enter first number:"))
    
    print("factorial value",num1,"is=",fact(num1))



elif select == 11 :
    num1=int(input("Enter first number:"))
    num2=int(input("Enter power number:"))
    print("square value ",num1,"^",num2,"=",square(num1,num2))

else:
    print("invalid opperation, pleace try again")
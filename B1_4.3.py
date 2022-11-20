from calc import *

def prog():
    print("Hello user"
          "Welcome in very simple calculator, when you can insert two numbers and output addition, substraction, multiplication or division")
    print("Please insert your numbers")

    a=float(input("a="))
    b=float(input("b="))

    print("Please insert number of action")
    print("1 - addition, 2 - substraction, 3 - multiplication, 4 - division")
    action=int(input("What is you action? "))

    if action==1:
        print(a,"+",b,"=",(addition(a,b)))
    elif action==2:
        print(a,"-",b,"=",(substraction(a,b)))
    elif action==3:
        print(a,"*",b,"=",(multiplication(a,b)))
    elif action==4:
        print(a,"/",b,"=",(division(a,b)))
    else:
        print("Wrong option, please insert value from 1 to 4")
prog()
#ax2+bx+c=0
import math

def equation(a,b,c):
    delta = -b/(4 * a * c)
    if a==0:
        print("a must be other from zero!!")
        exit()
    elif delta<0:
        print("There is no roots, because delta is less than zero")
    elif delta==0:
        x1=-b/(2*a)
        print("There is one root x=",x1)
    elif delta>0:
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        print("There is two roots, x1=",x1,"and x2=",x2)

def prog():
    print("Please insert values of coefficients in quadratic equation")
    a=float(input("a="))
    b=float(input("b="))
    c=float(input("c="))
    equation(a,b,c)

prog()

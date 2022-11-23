def pythagoreanTriangle(a,b,c):
    if a**2+b**2==c**2:
        print("This is Pythagorean triangle")
    else:
        print("This is not Pythagorean triangle")

def prog():
    print("This program is checking Pythagorean triangle - insert values of three sides")
    a=float(input("Insert a="))
    b=float(input("Insert b="))
    c=float(input("Insert c="))
    pythagoreanTriangle(a,b,c)

prog()
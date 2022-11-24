#greatest common divisior

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b, a % b)

def prog():
    a=int(input("Insert first number a="))
    b=int(input("Insert second number b="))

    print("Greatest common divisior for numbers",a,"and", b,"is", gcd(a,b))

prog()
def addition():
    c = a + b
    return c
def substraction():
    c = a - b
    return c
def multiplication():
    c = a*b
    return c
def division():
    c=a/b
    return c

a=int(input("Insert first number: "))
b=int(input("Insert second number: "))

if b == 0:
    print("b must be other from 0!")

print(f"Value of addition {a} + {b} = {addition()}")
print(f"Value of substraction {a} - {b} = {substraction()}")
print(f"Value of multiplication {a} * {b} = {multiplication()}")
print(f"Value of division {a} / {b} = {division()}")
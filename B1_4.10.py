def factorial(i):
    if i==0:
        return 1
    elif i!=0:
        return i*factorial(i-1)

def prog():
    for i in range(0,11):
        print(i,"!=",factorial(i))

prog()
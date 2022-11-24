#Triangular number

def triangularnum(n):
    if n==1:
        return 1
    else:
        return (n + triangularnum(n-1))
def prog():
    for i in range(1,11):
        print(i, "#=", triangularnum(i))

prog()
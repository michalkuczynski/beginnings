import math

def e(n):
    s,m=(1.0,1)
    for i in range (1,n):
        m=m*i
        s=s+1.0/m
    return s

def main():
    print("e=",math.e)
    print("calculated e=",e(20))

main()
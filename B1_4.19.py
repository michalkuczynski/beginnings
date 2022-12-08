def sum(n):
    s=0
    for i in range (1, n + 1):
        s=s+2*i-1
    return s

def main():
    print("sum of numbers=",sum(100))

main()
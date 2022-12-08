def sum(n):
    s=1
    for i in range (2, n + 1):
        if i % 2 == 0:
            s= s + i
        else:
            s = s - i
    return s
def main():
    print("sum of numbers=",sum(100))

main()
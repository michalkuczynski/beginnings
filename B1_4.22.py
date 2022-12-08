def addto(x):
    def add(y):
        return x + y
    return add

def main():
    addto15=addto(15)
    print(addto15(20))

main()
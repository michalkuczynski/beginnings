import random

class Sort():
    def __init__(self):
        print()

    def __del__(self):
        print()

    def sort(self,number):
        for i in range(len(number)-1,0,-1):
            for j in range(i):
                if number[j]>number[j+1]:
                    number[j],number[j+1]=number[j+1],number[j]

    def show(self,number):
        print("Sorted numbers: ",number)

def main():
    number=[]
    print("Program are generating 5 random numbers:")
    for i in range(1,6):
        i=random.randint(1,500)
        number.append(i)
        i+=1
    print("List =",number)
    noth=Sort()
    noth.sort(number)
    noth.show(number)

main()
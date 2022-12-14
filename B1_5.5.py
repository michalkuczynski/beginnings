class Person():
    def __init__(self):
        print()

    def worker(self):
        self.name=input("Insert name: ")
        self.lastname=input("Insert last name: ")
        self.street=input("Insert street: ")

    def display(self):
        print("Name: ",self.name,"Last name: ",self.lastname,"Street: ",self.street)

def main():
    Guy=Person()
    Guy.worker()
    Guy.display()

main()
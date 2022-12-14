class Person():
    def __init__(self):
        print()

    def worker(self):
        self.name=input("Insert name: ")
        self.lastname=input("Insert last name: ")
        self.street=input("Insert street: ")

    def display(self):
        print("Name: ",self.name,"Last name: ",self.lastname,"Street: ",self.street)

class OtherPerson(Person):
    def __init__(self):
        print()

    def worker2(self):
        self.profession=input("Insert worker profession: ")

    def display2(self):
        print("Profession: ",self.profession)

def main():
    Guy=Person()
    Guy2 = OtherPerson()
    Guy.worker()
    Guy2.worker2()
    Guy.display()
    Guy2.display2()

main()
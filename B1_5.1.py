class rectangle():
    def read(self):
        self.a=float(input("Insert value of first side a="))
        self.b=float(input("Insert value of second side b="))

    def processing(self):
        self.area=self.a*self.b
        return self.area

    def show(self):
        print("Area of rectangle with sides values a=",self.a,"b=",self.b,"is",self.area)

def main():
    area2=rectangle()
    area2.read()
    area2.processing()
    area2.show()

main()

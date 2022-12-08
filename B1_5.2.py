import math

class quadratic_equation():
    def read(self):
        self.a=float(input("Insert values of a="))
        if self.a==0:
            print("a must be other from 0!")
        else:
            self.b=float(input("Insert values of b="))
            self.c=float(input("Insert values of c="))

            self.delta=self.b**2-(4*self.a*self.c)

            if self.delta>0:
                self.x1 = (-self.b - math.sqrt(self.delta)) / (2 * self.a)
                self.x2 = (-self.b + math.sqrt(self.delta)) / (2 * self.a)
                print("x1=",self.x1,"x2=",self.x2)
            elif self.delta==0:
                self.x = -self.b/(2*self.a)
                print("x=",self.x)
            else:
                print("There is no roots, becase delta < 0")

def main():
    quadratic_equation_2=quadratic_equation()
    quadratic_equation_2.read()

main()

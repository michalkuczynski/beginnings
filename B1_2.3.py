#Zadanie 2.3 z książki PI
import math

a=float(input("Podaj wartość współczynnika a="))
b=float(input("Podaj wartość współczynnika b="))
c=float(input("Podaj wartość współczynnika c="))
delta=b**2-4*a*c
if a==0:
    print("Wartość współczynnika a musi być różna od zera")
elif delta>0:
    x1=(-b-math.sqrt(delta))/(2*a)
    x2=(-b+math.sqrt(delta))/(2*a)
    print(f"Pierwiastki równania kwadratowego to x1={x1} oraz x2={x2}")
elif delta==0:
    x=-b/(2*a)
    print(f"Równanie ma jeden pierwiastek x={x}")
elif delta<0:
    print(f"Równanie nie ma pierwiastków")
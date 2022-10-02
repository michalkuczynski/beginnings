#Zadanie 2.2 z książki PI

a=float(input("Podaj wartość współczynnika a="))
if a==0:
    print("Podana wartość musi być różna od zera")
else:
    b=float(input("Podaj wartość współczynnika b="))
    c=float(input("Podaj wartość współczynnika c="))
    x=(b-c)/a
    res = "{:.2f}".format(x)
    print(f"Wartość x wynosi {res}")
#Zadanie 2.1 z Książki PI

a=int(input("Podaj długość pierwszego boku: "))
b=int(input("Podaj długość drugiego boku: "))
c=int(input("Podaj długość trzeciego boku: "))

if a<0 or b<0 or c<0:
    print("Długości boków nie mogą być ujemne")

if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print("Trójkąt pitagorejski")
else:
    print("To nie jest trójkąt pitagorejski")
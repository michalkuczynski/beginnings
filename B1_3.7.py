#Zadnie 3.6 z ksiązki PI
import random
ilosc_liczb=5
suma=0
min=random.randint(0,100)
max=min
suma+=max
for i in range(ilosc_liczb):
    liczba=random.randint(0,100)
    print(liczba)
    if max<liczba:
        max=liczba
    if liczba<min:
        min=liczba
    suma+=liczba
print(f"Min number is {min}")
print(f"Max number is {max}")
print(suma)
avg=suma/ilosc_liczb
print(f"Average of 5 random numbers is {avg}")
#Zadanie 3.4 z książki PI

x=0
sum=0
while x<=100:
    if not (x%2==0):
        sum+=x
    x+=1
print(sum)
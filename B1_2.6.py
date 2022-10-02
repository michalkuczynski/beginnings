#Zadanie 2.6 z książki PI

a=True
b=True

leftside=not(a or b)
rightside=(not a) or (not b)

if leftside==rightside:
    print("Pierwsze Prawo de Morgana jest ok")
else:
    print("Przypał, nie jest ok")
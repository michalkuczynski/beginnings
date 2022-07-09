gra = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]


def plansza():
    for x in gra:
        for y in x:
            print(y, end=" ")

        print()


zawodnik = "O"
ile = 0

while (True):
    plansza()
    wsp = input(f"Zawodnik '{zawodnik}' podaj współrzędne: ")  # "12"
    wspY = int(wsp[0])  # "1"
    wspX = int(wsp[1])  # "2"

    if gra[wspY][wspX] != "*":
        print("pole zajęte")
    else:
        gra[wspY][wspX] = zawodnik
        ile += 1

    if (gra[0][0] == zawodnik and gra[1][1] == zawodnik and gra[2][2] == zawodnik):
        print(f"Wygrał zawodnik {zawodnik}")
        plansza()
        break
    elif (gra[0][2] == zawodnik and gra[1][1] == zawodnik and gra[2][0] == zawodnik):
        print(f"Wygrał zawodnik {zawodnik}")
        plansza()
        break
    elif (gra[0][0] == zawodnik and gra[0][1] == zawodnik and gra[0][2] == zawodnik):
        print(f"Wygrał zawodnik {zawodnik}")
        plansza()
        break
    elif (gra[1][0] == zawodnik and gra[1][1] == zawodnik and gra[1][2] == zawodnik):
        print(f"Wygrał zawodnik {zawodnik}")
        plansza()
        break
    elif (gra[2][0] == zawodnik and gra[2][1] == zawodnik and gra[2][2] == zawodnik):
        print(f"Wygrał zawodnik {zawodnik}")
        plansza()
        break
    elif (gra[0][0] == zawodnik and gra[1][0] == zawodnik and gra[2][0] == zawodnik):
        print(f"Wygrał zawodnik {zawodnik}")
        plansza()
        break
    elif (gra[0][1] == zawodnik and gra[1][1] == zawodnik and gra[2][1] == zawodnik):
        print(f"Wygrał zawodnik {zawodnik}")
        plansza()
        break
    elif (gra[0][2] == zawodnik and gra[1][2] == zawodnik and gra[2][2] == zawodnik):
        print(f"Wygrał zawodnik {zawodnik}")
        plansza()
        break

    if(ile == 9):
        print("Remis, koniec gry")
        break

    if (zawodnik == "O"):
        zawodnik = "X"
    else:
        zawodnik = "O"

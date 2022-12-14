import random

class Board():
    def __int__(self):
        print("Board 10 x , diagonally random numbers from 0 to 9")

    def drawboard(self,n,board):
        for i in range(n):
            for j in range(n):
                number=random.randint(1,9)
                if i==j:
                    board[i][j]=number
                else:
                    board[i][j]=0

        for i in range(n):
            for j in range(n):
                print(board[i][j]," ",end="")
                print()

    def sum(self,n,board):
        sum=0
        for i in range(n):
            sum+=board[i][i]
        print()
        print("Sum of diagonal numbers is ",sum)

def main():
    n=10
    board=[[0 for i in range(n)] for j in range(n)]
    matrice=Board()
    matrice.drawboard(n,board)
    matrice.sum(n,board)

main()

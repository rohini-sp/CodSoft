import tkinter as tk
import tkinter.messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(0,0)

        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(root, text='', font=('arial', 20), width=5, height=2,
                                                   command=lambda r=row, c=col: self.makeMove(r, c))
                self.buttons[row][col].grid(row=row, column=col)

    def makeMove(self, row, col):
        if self.board[row][col] == ' ' and self.current_player == 'X':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.checkWinner(self.current_player):
                self.endGame(f"{self.current_player} wins!")
            elif self.checkDraw():
                self.endGame("It's a draw!")
            else:
                self.current_player = 'O'
                self.aiMove()

    def aiMove(self):
        best_score = float('-inf')
        best_move = None

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    self.board[row][col] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[row][col] = ' '

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        if best_move:
            row, col = best_move
            self.board[row][col] = 'O'
            self.buttons[row][col].config(text='O')
            if self.checkWinner('O'):
                self.endGame("AI wins!")
            elif self.checkDraw():
                self.endGame("It's a draw!")
            else:
                self.current_player = 'X'

    def minimax(self, board, depth, is_maximizing):
        scores = {'X': -1, 'O': 1, 'draw': 0}

        if self.checkWinner('X'):
            return scores['X']
        if self.checkWinner('O'):
            return scores['O']
        if self.checkDraw():
            return scores['draw']

        if is_maximizing:
            max_eval = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = 'O'
                        eval = self.minimax(board, depth + 1, False)
                        board[row][col] = ' '
                        max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = 'X'
                        eval = self.minimax(board, depth + 1, True)
                        board[row][col] = ' '
                        min_eval = min(min_eval, eval)
            return min_eval

    def checkWinner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(row[col] == player for row in self.board):
                return True
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False


    def checkDraw(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def endGame(self, message):
        tk.messagebox.showinfo("Game Over", message)
        self.reset()

    def reset(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ' '
                self.buttons[row][col].config(text='')
        self.current_player = 'X'

def main():
    root = tk.Tk()
    tic_tac_toe = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        
        self.player1 = tk.StringVar()
        self.player2 = tk.StringVar()
        self.scoreboard = {"X": 0, "O": 0}
        
        self.get_player_names()

    def get_player_names(self):
        self.name_window = tk.Toplevel(self.window)
        self.name_window.title("Enter Player Names")
        
        tk.Label(self.name_window, text="Player 1 (X):").grid(row=0, column=0)
        tk.Entry(self.name_window, textvariable=self.player1).grid(row=0, column=1)
        
        tk.Label(self.name_window, text="Player 2 (O):").grid(row=1, column=0)
        tk.Entry(self.name_window, textvariable=self.player2).grid(row=1, column=1)
        
        tk.Button(self.name_window, text="Start Game", command=self.start_game).grid(row=2, columnspan=2)
    
    def start_game(self):
        self.name_window.destroy()
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []
        self.create_scoreboard()
        self.create_board()
    
    def create_scoreboard(self):
        self.score_label = tk.Label(self.window, text=f"{self.player1.get()} (X): {self.scoreboard['X']} | {self.player2.get()} (O): {self.scoreboard['O']}", font=("Arial", 14))
        self.score_label.grid(row=0, column=0, columnspan=3)
    
    def update_scoreboard(self):
        self.score_label.config(text=f"{self.player1.get()} (X): {self.scoreboard['X']} | {self.player2.get()} (O): {self.scoreboard['O']}")
    
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text=" ", font=("Arial", 24), height=2, width=5,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i+1, column=j)
                row.append(button)
            self.buttons.append(row)
    
    def make_move(self, i, j):
        index = i * 3 + j
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} ({self.player1.get() if self.current_player == 'X' else self.player2.get()}) wins!")
                self.scoreboard[self.current_player] += 1
                self.update_scoreboard()
                self.reset_board()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        win_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                        [0, 4, 8], [2, 4, 6]]
        for pattern in win_patterns:
            if self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] != " ":
                return True
        return False
    
    def reset_board(self):
        self.board = [" " for _ in range(9)]
        for row in self.buttons:
            for button in row:
                button.config(text=" ")
        self.current_player = "X"
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()

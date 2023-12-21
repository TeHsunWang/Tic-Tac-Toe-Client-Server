# player2.py
import socket
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from gameboard import BoardClass

class TicTacToePackerPlayer2:
    """Class representing the Tic-Tac-Toe Player 2 interface.

            Attributes:
                master (tk.Tk): The main Tkinter window.
                ip_address (tk.StringVar): Tkinter variable for storing the server's IP address.
                port (tk.IntVar): Tkinter variable for storing the server's port number.
                player1_name (tk.StringVar): Tkinter variable for storing Player 1's username.
                player2_name (tk.StringVar): Tkinter variable for storing Player 2's username.
                turn (bool): Flag indicating the current player's turn.
                board (BoardClass): Instance of the game board.
            """
    def __init__(self):
        """Initialize the TicTacToePackerPlayer2 instance."""
        self.master = tk.Tk()
        self.master.title("Tic-Tac-Toe Packer Player2")
        self.master.geometry('500x500')
        self.master.resizable(0, 0)

        self.ip_address = tk.StringVar()
        self.port = tk.IntVar()

        self.player1_name = tk.StringVar()
        self.player2_name = tk.StringVar()

        self.turn = False
        self.board = None

        self.create_widgets()

        self.runUI()

    def create_widgets(self):
        """Create the UI widgets for the player."""
        tk.Label(self.master, text="Enter Server IP Address").grid(row=0, column=0)
        tk.Entry(self.master, textvariable=self.ip_address).grid(row=0, column=1)

        tk.Label(self.master, text="Enter Server Port Number").grid(row=1, column=0)
        tk.Entry(self.master, textvariable=self.port).grid(row=1, column=1)

        tk.Label(self.master, text="Enter username, no special character").grid(row=2, column=0)
        tk.Entry(self.master, textvariable=self.player2_name).grid(row=2, column=1)

        tk.Button(self.master, text='Connect', command=self.connect).grid(row=3, column=0, columnspan=2)

    def connect(self):
        """Connect to the server and start the game."""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.ip_address.get(), self.port.get()))
        server_socket.listen(1)
        self.connection_socket, addr = server_socket.accept()
        # Receive Player 1's username
        self.player1_name.set(self.connection_socket.recv(1024).decode())
        # Send Player 2's username to Player 1
        self.connection_socket.send(self.player2_name.get().encode())
        self.Game()

    def Game(self):
        """Start the Tic-Tac-Toe game."""
        self.master.title("Tic Tac Toe Game Player2")
        self.board = BoardClass(self.player1_name.get(), self.player2_name.get())

        btn1 = ttk.Button(self.master, text=' ')
        btn1.grid(row=0, column=0, sticky='news', ipadx= 20, ipady=20)
        btn1.config(command=lambda: self.ButtonClick1(0, 0))
        self.btn1 = btn1

        btn2 = ttk.Button(self.master, text=' ')
        btn2.grid(row=0, column=1, sticky='news', ipadx= 20, ipady=20)
        btn2.config(command=lambda: self.ButtonClick2(0, 1))
        self.btn2 = btn2

        btn3 = ttk.Button(self.master, text=' ')
        btn3.grid(row=0, column=2, sticky='news', ipadx= 20, ipady=20)
        btn3.config(command=lambda: self.ButtonClick3(0, 2))
        self.btn3 = btn3

        btn4 = ttk.Button(self.master, text=' ')
        btn4.grid(row=1, column=0, sticky='news', ipadx= 20, ipady=20)
        btn4.config(command=lambda: self.ButtonClick4(1, 0))
        self.btn4 = btn4

        btn5 = ttk.Button(self.master, text=' ')
        btn5.grid(row=1, column=1, sticky='news', ipadx= 20, ipady=20)
        btn5.config(command=lambda: self.ButtonClick5(1, 1))
        self.btn5 = btn5

        btn6 = ttk.Button(self.master, text=' ')
        btn6.grid(row=1, column=2, sticky='news', ipadx= 20, ipady=20)
        btn6.config(command=lambda: self.ButtonClick6(1, 2))
        self.btn6 = btn6

        btn7 = ttk.Button(self.master, text=' ')
        btn7.grid(row=2, column=0, sticky='news', ipadx= 20, ipady=20)
        btn7.config(command=lambda: self.ButtonClick7(2, 0))
        self.btn7 = btn7

        btn8 = ttk.Button(self.master, text=' ')
        btn8.grid(row=2, column=1, sticky='news', ipadx= 20, ipady=20)
        btn8.config(command=lambda: self.ButtonClick8(2, 1,))
        self.btn8 = btn8

        btn9 = ttk.Button(self.master, text=' ')
        btn9.grid(row=2, column=2, sticky='news', ipadx= 20, ipady=20)
        btn9.config(command=lambda: self.ButtonClick9(2, 2))
        self.btn9 = btn9

        self.receive_move()

    def ButtonClick1(self, row, col):
        """Handle button click for position (0, 0)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'O')
            self.btn1['text'] = 'O'
            self.btn1.state(['disabled'])
            self.master.update()
            self.send_move(row, col)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
            else:
                # Receive opponent's move
                self.receive_move()
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick2(self, row, col):
        """Handle button click for position (0, 1)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'O')
            self.btn2['text'] = 'O'
            self.btn2.state(['disabled'])
            self.master.update()
            self.send_move(row, col)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
            else:
                # Receive opponent's move
                self.receive_move()
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick3(self, row, col):
        """Handle button click for position (0, 2)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'O')
            self.btn3['text'] = 'O'
            self.btn3.state(['disabled'])
            self.master.update()
            self.send_move(row, col)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
            else:
                # Receive opponent's move
                self.receive_move()
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick4(self, row, col,):
        """Handle button click for position (1, 0)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'O')
            self.btn4['text'] = 'O'
            self.btn4.state(['disabled'])
            self.master.update()
            self.send_move(row, col)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
            else:
                # Receive opponent's move
                self.receive_move()
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick5(self, row, col):
        """Handle button click for position (1,1)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'O')
            self.btn5['text'] = 'O'
            self.btn5.state(['disabled'])
            self.master.update()
            self.send_move(row, col)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
            else:
                # Receive opponent's move
                self.receive_move()
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick6(self, row, col):
        """Handle button click for position (1, 2)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'O')
            self.btn6['text'] = 'O'
            self.btn6.state(['disabled'])
            self.master.update()
            self.send_move(row, col)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
            else:
                # Receive opponent's move
                self.receive_move()
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick7(self, row, col):
        """Handle button click for position (2, 0)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'O')
            self.btn7['text'] = 'O'
            self.btn7.state(['disabled'])
            self.master.update()
            self.send_move(row, col)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
            else:
                # Receive opponent's move
                self.receive_move()
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick8(self, row, col):
        """Handle button click for position (2, 1)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'O')
            self.btn8['text'] = 'O'
            self.btn8.state(['disabled'])
            self.master.update()
            self.send_move(row, col)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
            else:
                # Receive opponent's move
                self.receive_move()
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick9(self, row, col):
        """Handle button click for position (2, 2)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'O')
            self.btn9['text'] = 'O'
            self.btn9.state(['disabled'])
            self.master.update()
            self.send_move(row, col)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
            else:
                # Receive opponent's move
                self.receive_move()
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def send_move(self, row, col):
        """Send the player's move to the opponent."""
        move_str = f"{row},{col}"
        self.connection_socket.sendall(move_str.encode())

    def receive_move(self):
        """Receive the opponent's move from the server."""
        move_str = self.connection_socket.recv(1024).decode()
        row, col = map(int, move_str.split(','))
        if row == 0 and col == 0:
            self.board.updateGameBoard(0, 0, 'X')
            self.btn1['text'] = 'X'
            self.btn1.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
        elif row == 0 and col == 1:
            self.board.updateGameBoard(0, 1, 'X')
            self.btn2['text'] = 'X'
            self.btn2.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
        elif row == 0 and col == 2:
            self.board.updateGameBoard(0, 2, 'X')
            self.btn3['text'] = 'X'
            self.btn3.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
        elif row == 1 and col == 0:
            self.board.updateGameBoard(1, 0, 'X')
            self.btn4['text'] = 'X'
            self.btn4.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
        elif row == 1 and col == 1:
            self.board.updateGameBoard(1, 1, 'X')
            self.btn5['text'] = 'X'
            self.btn5.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
        elif row == 1 and col == 2:
            self.board.updateGameBoard(1, 2, 'X')
            self.btn6['text'] = 'X'
            self.btn6.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
        elif row == 2 and col == 0:
            self.board.updateGameBoard(2, 0, 'X')
            self.btn7['text'] = 'X'
            self.btn7.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
        elif row == 2 and col == 1:
            self.board.updateGameBoard(2, 1, 'X')
            self.btn8['text'] = 'X'
            self.btn8.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
        elif row == 2 and col == 2:
            self.board.updateGameBoard(2, 2, 'X')
            self.btn9['text'] = 'X'
            self.btn9.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.receive_play_again()
        self.turn = True

    def resetGUIBoard(self):
        """Reset the GUI representation of the game board."""
        self.btn1['text'] = ' '
        self.btn2['text'] = ' '
        self.btn3['text'] = ' '
        self.btn4['text'] = ' '
        self.btn5['text'] = ' '
        self.btn6['text'] = ' '
        self.btn7['text'] = ' '
        self.btn8['text'] = ' '
        self.btn9['text'] = ' '

        self.btn1.state(['!disabled'])
        self.btn2.state(['!disabled'])
        self.btn3.state(['!disabled'])
        self.btn4.state(['!disabled'])
        self.btn5.state(['!disabled'])
        self.btn6.state(['!disabled'])
        self.btn7.state(['!disabled'])
        self.btn8.state(['!disabled'])
        self.btn9.state(['!disabled'])

    def receive_play_again(self):
        """Check if the player1 wants to play again."""
        self.turn = False
        play_again_msg = self.connection_socket.recv(1024).decode()
        if play_again_msg == 'yes':
            self.board.resetGameBoard()
            self.resetGUIBoard()
            self.Game()
        elif play_again_msg == 'Fun Time':
            self.show_stats()
            self.connection_socket.close()
            self.master.destroy()

    def show_game_end_message(self):
        """Display a message indicating the end of the game."""
        if self.board.isWinner('X'):
            messagebox.showinfo("Game Over", f"{self.player1_name.get()} wins!")
        elif self.board.isWinner('O'):
            messagebox.showinfo("Game Over", "You wins!")
        elif self.board.boardIsFull():
            messagebox.showinfo("Game Over", "It's a tie!")

    def show_stats(self):
        """Display the game statistics."""
        stats = self.board.computeStats()
        messagebox.showinfo('Game Stats', message=stats)
    def runUI(self):
        """Run the Tkinter main loop."""
        self.master.mainloop()

TicTacToePackerPlayer2()

import socket
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from gameboard import BoardClass

class TicTacToePackerPlayer1:
    """Class representing the Tic-Tac-Toe Player 1 interface.

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
        """Initialize the TicTacToePackerPlayer1 instance."""
        self.master = tk.Tk()
        self.master.title("Tic-Tac-Toe Player 1")
        self.master.geometry('500x500')
        self.master.resizable(0, 0)

        self.ip_address = tk.StringVar()
        self.port = tk.IntVar()
        self.player1_name = tk.StringVar()
        self.player2_name = tk.StringVar()

        self.turn = True
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
        tk.Entry(self.master, textvariable=self.player1_name).grid(row=2, column=1)

        tk.Button(self.master, text='Connect', command=self.connect).grid(row=3, column=0, columnspan=2)

    def connect(self):
        """Connect to the server and start the game."""
        try:
            # Connect to Player 2
            connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection_socket.connect((self.ip_address.get(), self.port.get()))
            # Send Player 1's username
            connection_socket.sendall((self.player1_name.get().encode()))
            # Receive Player 2's username
            p1 = connection_socket.recv(1024).decode()
            self.player2_name.set(p1)
            # Start the game after getting Player 2's name
            self.Game(connection_socket)
            return connection_socket

        except Exception as e:
            print(f'Connection Error: {e}')
            self.prompt_retry_window()

    def prompt_retry_window(self):
        """Display a retry window in case of connection error."""
        retry_window = tk.Toplevel(self.master)
        retry_window.title("Connection Error")

        tk.Label(retry_window, text="Connection Error. Do you want to try again?").grid(row=0, column=0)

        def on_yes():
            retry_window.destroy()

        tk.Button(retry_window, text='Yes', command=on_yes).grid(row=1, column=0)
        tk.Button(retry_window, text='No', command=self.master.destroy).grid(row=1, column=1)

    def Game(self, connection_socket):
        """Start the Tic-Tac-Toe game. And initialize buttons"""
        self.master.title("Tic Tac Toe Game Player1")

        self.board = BoardClass(self.player1_name.get(), self.player2_name.get())

        btn1 = ttk.Button(self.master, text = ' ')
        btn1.grid(row=0, column=0, sticky='news', ipadx= 20, ipady=20)
        btn1.config(command=lambda: self.ButtonClick1(0,0,connection_socket))
        self.btn1 = btn1

        btn2 = ttk.Button(self.master, text=' ')
        btn2.grid(row=0, column=1, sticky='news', ipadx= 20, ipady=20)
        btn2.config(command=lambda: self.ButtonClick2(0,1,connection_socket))
        self.btn2 = btn2

        btn3 = ttk.Button(self.master, text=' ')
        btn3.grid(row=0, column=2, sticky='news',ipadx= 20, ipady=20)
        btn3.config(command=lambda: self.ButtonClick3(0,2,connection_socket))
        self.btn3 = btn3

        btn4 = ttk.Button(self.master, text=' ')
        btn4.grid(row=1, column=0, sticky='news', ipadx= 20, ipady=20)
        btn4.config(command=lambda: self.ButtonClick4(1,0,connection_socket))
        self.btn4 = btn4

        btn5 = ttk.Button(self.master, text=' ')
        btn5.grid(row=1, column=1, sticky='news',ipadx= 20, ipady=20)
        btn5.config(command=lambda: self.ButtonClick5(1,1,connection_socket))
        self.btn5 = btn5

        btn6 = ttk.Button(self.master, text=' ')
        btn6.grid(row=1, column=2, sticky='news', ipadx= 20, ipady=20)
        btn6.config(command=lambda: self.ButtonClick6(1,2,connection_socket))
        self.btn6 = btn6

        btn7 = ttk.Button(self.master, text=' ')
        btn7.grid(row=2, column=0, sticky='news', ipadx= 20, ipady=20)
        btn7.config(command=lambda: self.ButtonClick7(2,0,connection_socket))
        self.btn7 = btn7

        btn8 = ttk.Button(self.master, text=' ')
        btn8.grid(row=2, column=1, sticky='news', ipadx= 20, ipady=20)
        btn8.config(command=lambda: self.ButtonClick8(2,1,connection_socket))
        self.btn8 = btn8

        btn9 = ttk.Button(self.master, text=' ')
        btn9.grid(row=2, column=2, sticky='news', ipadx= 20, ipady=20)
        btn9.config(command=lambda: self.ButtonClick9(2,2,connection_socket))
        self.btn9 = btn9

    def ButtonClick1(self, row, col,connection_socket):
        """Handle button click for position (0, 0)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'X')
            self.btn1['text'] = 'X'
            self.btn1.state(['disabled'])
            self.master.update()
            self.send_move(row, col, connection_socket)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
            else:
                # Receive opponent's move
                self.receive_move(connection_socket)
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick2(self, row, col,connection_socket):
        """Handle button click for position (0, 1)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'X')
            self.btn2['text'] = 'X'
            self.btn2.state(['disabled'])
            self.master.update()
            self.send_move(row, col, connection_socket)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
            else:
                # Receive opponent's move
                self.receive_move(connection_socket)
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick3(self, row, col,connection_socket):
        """Handle button click for position (0, 2)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'X')
            self.btn3['text'] = 'X'
            self.btn3.state(['disabled'])
            self.master.update()
            self.send_move(row, col, connection_socket)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
            else:
                # Receive opponent's move
                self.receive_move(connection_socket)
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick4(self, row, col,connection_socket):
        """Handle button click for position (1, 0)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'X')
            self.btn4['text'] = 'X'
            self.btn4.state(['disabled'])
            self.master.update()
            self.send_move(row, col, connection_socket)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
            else:
                # Receive opponent's move
                self.receive_move(connection_socket)
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick5(self, row, col,connection_socket):
        """Handle button click for position (1, 1)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'X')
            self.btn5['text'] = 'X'
            self.btn5.state(['disabled'])
            self.master.update()
            self.send_move(row, col, connection_socket)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
            else:
                # Receive opponent's move
                self.receive_move(connection_socket)
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick6(self, row, col,connection_socket):
        """Handle button click for position (1, 2)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'X')
            self.btn6['text'] = 'X'
            self.btn6.state(['disabled'])
            self.master.update()
            self.send_move(row, col,connection_socket)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
            else:
                # Receive opponent's move
                self.receive_move(connection_socket)
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick7(self, row, col,connection_socket):
        """Handle button click for position (2, 0)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'X')
            self.btn7['text'] = 'X'
            self.btn7.state(['disabled'])
            self.master.update()
            self.send_move(row, col,connection_socket)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
            else:
                # Receive opponent's move
                self.receive_move(connection_socket)
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick8(self, row, col,connection_socket):
        """Handle button click for position (2, 1)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'X')
            self.btn8.config(text='X')
            self.btn8.state(['disabled'])
            self.master.update()
            self.send_move(row, col,connection_socket)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
            else:
                # Receive opponent's move
                self.receive_move(connection_socket)
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")

    def ButtonClick9(self, row, col,connection_socket):
        """Handle button click for position (2, 2)."""
        if self.turn:
            self.board.updateGameBoard(row, col, 'X')
            self.btn9['text'] = 'X'
            self.btn9.state(['disabled'])
            self.master.update()
            self.send_move(row, col,connection_socket)
            self.turn = False
            # Check for game over
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
            else:
                # Receive opponent's move
                self.receive_move(connection_socket)
                self.turn = True
        else:
            messagebox.showerror("It's not your turn yet")
    def send_move(self, row, col,connection_socket):
        """Send the player's move to the opponent."""
        move_str = f"{row},{col}"
        connection_socket.sendall(move_str.encode())

    def receive_move(self,connection_socket):
        """Receive the opponent's move from the server."""
        move_str = connection_socket.recv(1024).decode()
        row = int(move_str[0])
        col = int(move_str[2])
        if row==0 and col==0:
            self.board.updateGameBoard(0,0,'O')
            self.btn1['text'] = 'O'
            self.btn1.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
        elif row==0 and col==1:
            self.board.updateGameBoard(0,1,'O')
            self.btn2['text'] = 'O'
            self.btn2.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
        elif row==0 and col==2:
            self.board.updateGameBoard(0,2,'O')
            self.btn3['text'] = 'O'
            self.btn3.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
        elif row==1 and col==0:
            self.board.updateGameBoard(1,0,'O')
            self.btn4['text'] = 'O'
            self.btn4.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
        elif row==1 and col==1:
            self.board.updateGameBoard(1,1,'O')
            self.btn5['text'] = 'O'
            self.btn5.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
        elif row==1 and col==2:
            self.board.updateGameBoard(1,2,'O')
            self.btn6['text'] = 'O'
            self.btn6.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
        elif row==2 and col==0:
            self.board.updateGameBoard(2,0,'O')
            self.btn7['text'] = 'O'
            self.btn7.state(['disable'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
        elif row==2 and col==1:
            self.board.updateGameBoard(2,1,'O')
            self.btn8['text'] = 'O'
            self.btn8.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
        elif row==2 and col==2:
            self.board.updateGameBoard(2,2,'O')
            self.btn9['text'] = 'O'
            self.btn9.state(['disabled'])
            self.master.update()
            if self.board.isGameOver():
                self.show_game_end_message()
                self.ask_play_again(connection_socket)
        self.turn = True

    def ask_play_again(self,connection_socket):
        """Ask the player if they want to play again."""
        answer = messagebox.askquestion("Play Again?", "Do you want to play again?")
        if answer == 'yes':
            self.board.resetGameBoard()
            self.resetGUIBoard()
            connection_socket.sendall('yes'.encode())
            self.turn = True
            self.Game(connection_socket)
        else:
            messagebox.showinfo("Fun Time!")
            self.show_stats()
            connection_socket.sendall('Fun Time'.encode())
            self.master.destroy()

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

    def show_game_end_message(self):
        """Display a message indicating the end of the game."""
        if self.board.isWinner('X'):
            messagebox.showinfo("Game Over", "You win!")
        elif self.board.isWinner('O'):
            messagebox.showinfo("Game Over", f"{self.player2_name.get()} wins!")
        elif self.board.boardIsFull():
            messagebox.showinfo("Game Over", "It's a tie!")

    def show_stats(self):
        """Display the game statistics."""
        stats = self.board.computeStats()
        messagebox.showinfo('Game Stats', message=stats)
    def runUI(self):
        """Run the Tkinter main loop."""
        self.master.mainloop()

if __name__ == "__main__":
    TicTacToePackerPlayer1()

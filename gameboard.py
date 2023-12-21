class BoardClass():
    """Represents a tic-tac-toe game board.


        Attributes:
            player_name (str): The name of the player.
            games_played (int): The number of games played.
            tie (int): The number of ties.
            win (int): The number of wins.
            lose (int): The number of losses.
            last_player_turn (str): The user name of the last player to make a move.
            board (List[List[str]]): The tic-tac-toe game board.
    """
    def __init__(self, player1_name, player2_name) -> None:
        """Initialize the BoardClass.
           Args:
               player1_name: The name of the player1.
               player2_name: The name of the player2
        """
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.games_played = 0
        self.tie = 0
        self.win = 0
        self.lose = 0
        self.last_player_turn = None
        # Initialize board
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def updateGamesPlayed(self) -> None:
        """Update the number of games played."""
        self.games_played += 1
    def resetGameBoard(self) -> None:
        """Reset the game board and print it."""
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.last_player_turn = None

    def is_valid_move(self, row: int, col: int) -> bool:
        """Check if the specified move is valid.

        Args:
            row (int): The row index of the move.
            col (int): The column index of the move.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        try:
            row, col = map(int, (row, col))
            if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
                return True
            else:
                return False
        except ValueError:
            return False

    def updateGameBoard(self, row: int, col: int, symbol: str) -> bool:
        """Update the game board with the specified move.

        Args:
            row (int): The row index of the move.
            col (int): The column index of the move.
            symbol (str): The symbol to update the board with ('X' or 'O').

        Returns:
            bool: True if the move is valid and successfully updated, False otherwise.
        """
        if not self.isGameOver() and self.is_valid_move(row, col):
            self.board[row][col] = symbol
            self.last_player_turn = 'Player1' if symbol == 'X' else 'Player2'
            if self.isWinner(symbol):
                if symbol == 'X':
                    self.win += 1
                elif symbol == 'O':
                    self.lose += 1
                self.updateGamesPlayed()
                return True
            if self.boardIsFull():
                self.tie += 1
                self.updateGamesPlayed()
                return True
            return False
        else:
            return False
    def isGameOver(self) -> bool:
        """Check if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.isWinner('X') or self.isWinner('O') or self.boardIsFull()

    def isWinner(self, symbol: str) -> bool:
        """Check if the specified symbol has won the game.

        Args:
            symbol (str): The symbol to check for a win ('X' or 'O').

        Returns:
            bool: True if the symbol has won, False otherwise.
        """
        if all(self.board[0][i] == symbol for i in range(3)): #check win for row 0
            return True
        elif all(self.board[1][i] == symbol for i in range(3)): #check win for row 1
            return True
        elif all(self.board[2][i] == symbol for i in range(3)): #check win for row 2
            return True
        elif all(self.board[i][0] == symbol for i in range(3)): #check win for col 0
            return True
        elif all(self.board[i][1] == symbol for i in range(3)): #check win for col 1
            return True
        elif all(self.board[i][2] == symbol for i in range(3)): #check win for col 2
            return True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol: #check diagonal
            return True
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] == symbol:
            return True
        else:
            return False
    def boardIsFull(self) -> bool:
        """Check if the game board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        if all(self.board[i][j] != ' 'for i in range(3) for j in range(3)):
            return True

    def computeStats(self):
        """Return the statistics of the game."""

        #Prints the players user name, the user name of the last person to make a move, the number of games
        #the number of wins, the number of losses, the number of ties
        stats = (
            f'Player1 name: {self.player1_name}',
            f'Player2 name: {self.player2_name}',
            f'Last person make a move: {self.last_player_turn}',
            f'Number of games: {self.games_played}',
            f'Number of wins of player1: {self.win}',
            f'Number of losses of player1: {self.lose}',
            f'Number of wins of player2: {self.lose}',
            f'Number of losses of player2: {self.win}',
            f'Number of ties: {self.tie}'
        )

        return '\n'.join(stats)

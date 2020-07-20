class TicTacToe:
    '''A simple Tic-tac-toe gam'''

    def __init__(self):
        self.move = 0
        self.game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def display(self):
        print('---------')
        for row in self.game_board:
            print('| ', end = '')
            for elem in row:
                print(elem, end = ' ')
            print('|')
        print('---------')

    def user_move(self):
        while True:
            try:
                coordinates = [int(x) for x in input('Enter the coordinates: ').split()]
                if len(coordinates) == 2:
                    row = 3 - coordinates[1]
                    column = coordinates[0] - 1
                else:
                    print('Enter a valid coordinate!')
                    continue

                if max(coordinates) > 3 or min(coordinates) < 1:
                    print('Coordinates should be from 1 to 3!')
                    continue

                if self.game_board[row][column] != ' ':
                    print('This cell is occupied! Choose another one!')
                    continue

            except ValueError:
                print('You should enter numbers!')
                continue

            if self.move % 2 == 0:
                self.game_board[row][column] = 'X'
            else:
                self.game_board[row][column] = 'O'

            self.move += 1
            self.display()
            break

    def check_game_state(self):
        winner = ''
        column_wins = [[x[i] for x in self.game_board] for i in range(3)]
        diagonal_wins = [[self.game_board[0][0], self.game_board[1][1], self.game_board[2][2]], [self.game_board[0][2], self.game_board[1][1], self.game_board[2][0]]]
        if ['X', 'X', 'X'] in game.game_board or ['X', 'X', 'X'] in column_wins or ['X', 'X', 'X'] in diagonal_wins:
            winner = 'X'
        elif ['O', 'O', 'O'] in game.game_board or ['O', 'O', 'O'] in column_wins or ['O', 'O', 'O'] in diagonal_wins:
            winner = 'O'

        if winner:
            print(winner, 'wins')
            return False
        elif self.move == 9:
            print('Draw!')
            return False

        return True


game = TicTacToe()
run = True
game.display()
while run:
    game.user_move()
    run = game.check_game_state()

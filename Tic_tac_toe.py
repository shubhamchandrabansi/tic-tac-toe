# Tic - tac - toe (File name - Tic_tac_toe.py)
# made by Shubham Kumar Chandrabansi
# UID: 20BCS9777

#setting inital state of board
mark = [' '] * 10
mark[0] = "-"

# prints the present state of board
def board():
    print("┌───┬───┬───┐")
    print('│ ' + mark[1] + ' │ ' + mark[2] + ' │ ' + mark[3] + ' │')
    print("├───┼───┼───┤")
    print('│ ' + mark[4] + ' │ ' + mark[5] + ' │ ' + mark[6] + ' │')
    print("├───┼───┼───┤")
    print('│ ' + mark[7] + ' │ ' + mark[8] + ' │ ' + mark[9] + ' │')
    print("└───┴───┴───┘")


# checks if a player has won
def win(sign):
    return ((mark[1] == mark[2] == mark[3] == sign) or (mark[4] == mark[5] == mark[6] == sign) or (
            mark[7] == mark[8] == mark[9] == sign) or (mark[1] == mark[5] == mark[9] == sign) or (
                    mark[3] == mark[5] == mark[7] == sign) or (mark[1] == mark[4] == mark[7] == sign) or (
                    mark[2] == mark[5] == mark[8] == sign) or (mark[3] == mark[6] == mark[9] == sign))


# checks whether a place on the board is empty or not
def blank(place):
    return mark[place] == ' '


# Alternates players based on their turn
def game():
    turn = 'first'
    while 1:
        if ' ' not in mark:  # check if the match has ended in a draw
            print('Draw')
            break
        elif turn == 'first':
            print('Player X turn')
            place = int(input('Enter where you want to place X: '))
            if blank(place):
                mark[place] = 'X'
                board()
                if win('X'):
                    print('Player X wins')
                    break
                else:
                    turn = 'second'
            else:
                print('Please give correct position. Try again !')

        elif turn == 'second':
            print('Player O turn')
            place = int(input('Enter where you want to place O: '))
            if blank(place):
                mark[place] = 'O'
                board()
                if win('O'):
                    print('Player O wins')
                    break
                else:
                    turn = 'first'
            else:
                print('Please give correct position. Try again !')


# Main Menu
if __name__ == '__main__':
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("│          Welcome to Tic-Tac-Toe           │")
    print("│   Written by Shubham Kumar Chandrabansi   │")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # Instructions for playing
    print('''
    The positions are as follows
    ┌───┬───┬───┐
    | 1 | 2 | 3 |
    ├───┼───┼───┤
    | 4 | 5 | 6 |
    ├───┼───┼───┤
    | 7 | 8 | 9 |
    └───┴───┴───┘
    BEST OF LUCK !!
    ''')

    # allows user to play game until they want to quit
    while 1:
        game()
        # resetting board position to default position
        mark = [' '] * 10
        mark[0] = "-"
        replay = input("Replay 'Y' OR 'N'").upper()
        if replay == 'Y':
            print('''
                The positions are as follows
                ┌───┬───┬───┐
                | 1 | 2 | 3 |
                ├───┼───┼───┤
                | 4 | 5 | 6 |
                ├───┼───┼───┤
                | 7 | 8 | 9 |
                └───┴───┴───┘
                BEST OF LUCK !!
                ''')
            continue
        else:
            print('Thank you')
            break

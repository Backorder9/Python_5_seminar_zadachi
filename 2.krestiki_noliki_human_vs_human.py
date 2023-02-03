'''
Создайте программу для игры в 'Крестики-нолики'
НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом.
'''
vse_kletki = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '


def main():
    print('Сыграем в крестики-нолики!')
    gameBoard = chistaya_doska()
    currentPlayer, nextPlayer = X, O

    while True:
        print(v_dosku(gameBoard))
        move = None
        while not kletka_svobodna(gameBoard, move):
            print('Ход игрока {} (1-9)'.format(currentPlayer))
            move = input('> ')
        obnoviti_dosku(gameBoard, move, currentPlayer)

        if Pobeditelh(gameBoard, currentPlayer):
            print(v_dosku(gameBoard))
            print(currentPlayer + ' выиграл!')
            break
        elif doska_polna(gameBoard):
            print(v_dosku(gameBoard))
            print('Ничья!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Хорошо сыграли!')


def chistaya_doska():
    board = {}
    for space in vse_kletki:
        board[space] = BLANK
    return board


def v_dosku(board):
    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'],
                                board['4'], board['5'], board['6'],
                                board['7'], board['8'], board['9'])

def kletka_svobodna(board, space):
    return space in vse_kletki and board[space] == BLANK


def Pobeditelh(board, player):
    b, p = board, player
    return ((b['1'] == b['2'] == b['3'] == p) or
            (b['4'] == b['5'] == b['6'] == p) or
            (b['7'] == b['8'] == b['9'] == p) or
            (b['1'] == b['4'] == b['7'] == p) or
            (b['2'] == b['5'] == b['8'] == p) or
            (b['3'] == b['6'] == b['9'] == p) or
            (b['3'] == b['5'] == b['7'] == p) or
            (b['1'] == b['5'] == b['9'] == p))

def doska_polna(board):
    for space in vse_kletki:
        if board[space] == BLANK:
            return False
    return True


def obnoviti_dosku(board, space, mark):
    board[space] = mark


if __name__ == '__main__':
    main()

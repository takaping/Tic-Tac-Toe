def draw_stage(cell_list):
    index = 0
    print('-' * 9)
    for row in range(3):
        row_string = '| '
        for col in range(3):
            cell = ' '
            if cell_list[index] != '_':
                cell = cell_list[index]
            row_string += (cell + ' ')
            index += 1
        row_string += '|'
        print(row_string)
    print('-' * 9)


def place_piece(player, cell_list):
    placed = False
    while not placed:
        coords = input('Enter the coordinates: ')
        try:
            col, row = [int(num) for num in coords.split()]
            index = (3 - row) * 3 + (col - 1)
            if (col < 1 or col > 3) or (row < 1 or row > 3):
                print('Coordinates should be from 1 to 3!')
            elif cell_list[index] != '_':
                print('This cell is occupied! Choose another one!')
            else:
                cell_list[index] = player
                placed = True
        except ValueError:
            print('You should enter numbers!')


def is_win(cells, symbol):
    for col in range(0, 9, 3):
        if cells[col:col + 3].count(symbol) == 3:
            return True
    for col in range(3):
        tmp = cells[col:]
        if tmp[:9:3].count(symbol) == 3:
            return True
    if cells[:9:4].count(symbol) == 3:
        return True
    tmp = cells[2:]
    if tmp[:5:2].count(symbol) == 3:
        return True
    return False


def get_status(cell_list):
    num_x = cell_list.count('X')
    num_o = cell_list.count('O')
    num_b = cell_list.count('_')
    x_wins = is_win(cell_list, 'X')
    o_wins = is_win(cell_list, 'O')

    if (x_wins and o_wins) \
            or (abs(num_x - num_o) > 1):
        return 'Impossible'
    elif x_wins:
        return 'X wins'
    elif o_wins:
        return 'O wins'
    elif num_b == 0:
        return 'Draw'
    return 'Game not finished'


players = ('X', 'O')
cells = '_________'
cell_list = [symbol for symbol in cells]
player_num = 0

draw_stage(cell_list)
while True:
    place_piece(players[player_num], cell_list)
    draw_stage(cell_list)
    msg = get_status(cell_list)
    if msg != 'Game not finished':
        print(msg)
        break
    player_num = (player_num + 1) % 2

fl = True
while fl:
    print("*" * 23)
    print("Welcome to Tic-Tac-Toe!")
    print("*" * 23)

    grid = ['_', '_', '_',
            '_', '_', '_',
            '_', '_', '_', ]


    def DrawGrid(grid):
        print("-" * 13)
        [print("|", grid[0 + i * 3], "|", grid[1 + i * 3], "|", grid[2 + i * 3], "|") for i in range(3)]
        print("-" * 13)

    def PlayerTurnToNumber(row, col):
        if row == 1 and col == 1:
            return 1
        if row == 1 and col == 2:
            return 2
        if row == 1 and col == 3:
            return 3
        if row == 2 and col == 1:
            return 4
        if row == 2 and col == 2:
            return 5
        if row == 2 and col == 3:
            return 6
        if row == 3 and col == 1:
            return 7
        if row == 3 and col == 2:
            return 8
        if row == 3 and col == 3:
            return 9


    def PlayerTurn(player):
        valid = False
        while not valid:
            player_turn_row = int(input(f'Please enter row for {player}: '))
            player_turn_col = int(input(f'Please enter column for {player}: '))
            if player_turn_row in range(1, 4) and player_turn_col in range(1, 4):
                player_turn = PlayerTurnToNumber(player_turn_row, player_turn_col)

                if str(grid[player_turn - 1]) not in "XO":
                    grid[player_turn - 1] = player
                    valid = True
                else:
                    print("This cell is already taken!")
            else:
                print("!!! Invalid input. \nTry again, enter number from 1 to 3?")


    def CheckWin(grid):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if grid[each[0]] == grid[each[1]] == grid[each[2]]:
                return grid[each[0]]
        return False


    def game(grid):
        counter = 0
        win = False
        while not win:
            DrawGrid(grid)
            if counter % 2 == 0:
                PlayerTurn("X")
            else:
                PlayerTurn("O")
            counter += 1
            if counter > 4:
                player = CheckWin(grid)
                if player:
                    print(player, "Win!")
                    break
            if counter == 9:
                print("Dead heat!")
                break
        DrawGrid(grid)


    game(grid)

    exit_fl = input("Exit? y/n: ")
    if exit_fl == 'y':
        fl = False
    else:
        fl = True

import os
from sys import platform
from battleships import *


"""
Clears terminal output for different OS. Makes the terminal look cleaner when printing the board after each shot.
Defines lambda function clear().
"""
if "linux" == platform or "linux2" == platform or "darwin" == platform:
    clear = lambda: os.system('clear')
elif "win32" == platform:
    clear = lambda: os.system('cls')


def print_board(board):
    """
    Prints out a board to the required specifications.
    :param board: a 10*10 matrix of symbols, indicating a tile's status (e.g. hit, miss, not shot at)
    :return: a board with numbered rows and columns
    """
    print("     0   1   2   3   4   5   6   7   8   9")
    print("     -------------------------------------")
    for i in range(10):
        print(i, "|", " ", end="")
        for j in range(10):
            print(board[i][j], end="")
        print("")


def mark_sunk_ship(ship_hit, board):
    """
    Once a ship has been sunk, it marks each of the tiles that ship occupied on the board
    with a letter denoting the ship's name (e.g. B for battleship, C for cruiser etc.)
    :param ship_hit: the ship that has been sunk
    :param board: a 10*10 matrix of symbols, indicating a tile's status (e.g. hit, miss, not shot at)
    :return: updates the board with the necessary changes
    """
    ship_length = ship_hit[3]
    hits = ship_hit[4]

    if ship_length == 1:
        board[ship_hit[0]][ship_hit[1]] = "S   "
    elif ship_length == 2:
        for x in hits:
            board[x[0]][x[1]] = "D   "
    elif ship_length == 3:
        for x in hits:
            board[x[0]][x[1]] = "C   "
    elif ship_length == 4:
        for x in hits:
            board[x[0]][x[1]] = "B   "


def main():
    """
    Implements the same as main() in battleships.py but with the visual extension elements included.
    Inline comments are in battleships.py file.
    """
    current_fleet = randomly_place_all_ships()
    print("Let's play battleships!")
    print("Enter 'quit' to exit the game.")

    game_over = False
    shots = 0
    chose_to_quit = False
    cache_shots = set()

    pattern = re.compile("^[+-]?[0-9]+$")

    board = [[".   " for i in range(10)] for j in range(10)]
    miss_marker = "-   "
    hit_marker = "*   "

    while not game_over:
        shot_str = input("Enter row and column to shoot (separated by space): ").split()
        if len(shot_str) != 2:
            if len(shot_str) == 1 and shot_str[0] == "quit":
                chose_to_quit = True
                break
            else:
                print("Invalid entry, try again!")

        else:
            if pattern.match(str(shot_str[0])) and pattern.match(str(shot_str[1])):
                if 0 <= int(shot_str[0]) <= 9 and 0 <= int(shot_str[1]) <= 9:
                    current_row = int(shot_str[0])
                    current_column = int(shot_str[1])
                    shots += 1
                    if (current_row, current_column) not in cache_shots:
                        cache_shots.add((current_row, current_column))
                        if check_if_hits(current_row, current_column, current_fleet):
                            board[current_row][current_column] = hit_marker
                            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
                            if is_sunk(ship_hit):
                                mark_sunk_ship(ship_hit, board)
                                clear()
                                print_board(board)
                                print("You have a hit!")
                                print("You sank a " + ship_type(ship_hit) + "!")
                            else:
                                clear()
                                print_board(board)
                                print("You have a hit!")
                        else:
                            clear()
                            board[current_row][current_column] = miss_marker
                            print_board(board)
                            print("You missed!")
                    else:
                        clear()
                        print_board(board)
                        print("You've already shot here! Try another tile.")

                else:
                    print("Invalid entry - shot out of range! Try again!")
            else:
                print("Invalid entry, try again!")

        if not are_unsunk_ships_left(current_fleet):
            game_over = True

    if chose_to_quit:
        print("Finished already? You only took", shots, "shots. See you next time!")
    else:
        print("Game over! You required", shots, "shots.")


if __name__ == '__main__':
    main()

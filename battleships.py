import re
from random import *


def is_sunk(ship):
    """
    Returns boolean True if ship is sunk, otherwise False. Determined by the number
    of hits on the ship and the ship's length.
    :param ship: ship is a group of tuples (e.g. row, column, horizontal, length, hits)
    :return: Boolean, indicating if ship is sunk or not
    """
    length = ship[3]
    num_hits = len(ship[4])
    return length == num_hits


def ship_type(ship):
    """
    Returns a string with the ship name, determined by ship_length.
    :param ship: ship is a group of tuples (e.g. row, column, horizontal, length, hits)
    :return: The string ship name
    """
    ship_length = ship[3]
    if ship_length == 4:
        return "battleship"
    elif ship_length == 3:
        return "cruiser"
    elif ship_length == 2:
        return "destroyer"
    elif ship_length == 1:
        return "submarine"


def occupied_tiles(fleet):
    """
    Returns a list of all occupied tiles on the board.
    An occupied tile is a tile containing a ship or part of a ship.
    :param fleet: fleet is a list of ship tuple objects e.g. [(row, column, horizontal, length, hits),...]
    :return: the tile_list of occupied tiles on the board, determined by the ships in the fleet
    """
    tile_list = []

    for ship in fleet:
        ship_row = ship[0]  # upper left row coordinate of ship
        ship_column = ship[1]  # upper left column coordinate of ship
        horizontal = ship[2]
        length = ship[3]
        if horizontal:
            # if ship is horizontal, iterates through ship's column coordinates
            # appends each coordinate to the tile_list (as a tuple of row, column), which contains a ship
            for i in range(ship_column, ship_column + length):
                tile_list.append((ship_row, i))
        else:
            # if ship is vertical, iterates through ship's row coordinates & appends to tile_list
            for i in range(ship_row, ship_row + length):
                tile_list.append((i, ship_column))

    return tile_list


def is_open_sea(row, column, fleet):
    """
    Checks if the tile, specified by (row, column), and any of the 8 surrounding tiles contains a ship
    by calling occupied_tiles(fleet) and checking if the tuple coordinate is in the list.
    :param row: the row number of the tile, as an int between 0-9
    :param column: the column number of the tile, as an int between 0-9
    :param fleet: fleet is a list of ship tuple objects e.g. [(row, column, horizontal, length, hits),...]
    :return: returns a boolean True if the tile is open sea, otherwise False
    """
    result = True
    # drow - the list of 8 possible movements on the row-axis towards an adjacent tile (maps onto dcolumn)
    # dcolumn - the list of 8 possible movements on the column-axis towards an adjacent tile
    drow = [0, 1, 1, 0, -1, -1, -1, 0, 1]
    dcolumn = [0, 0, 1, 1, 1, 0, -1, -1, -1]

    # checks if a tile, or any of its adjacent tiles, contain a ship or ship part, by using occupied_tiles
    # if so, then tile is not open sea and returns false
    for i in range(len(drow)):
        if (row + drow[i], column + dcolumn[i]) in occupied_tiles(fleet):
            result = False
            break

    # if tile is out of bounds it is also not open sea
    if row > 9 or row < 0 or column > 9 or column < 0:
        result = False

    return result


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    """
    Determines if a ship can be placed at a specific location on the board, by checking
    if all ship's tiles and all adjacent tiles are open sea.
    :param row: the row number of the tile as an int between 0-9, representing the upper left coord of a ship
    :param column: the column number of the tile as an int between 0-9, representing the upper left coord of a ship
    :param horizontal: a boolean indicating that a ship is placed horizontally if True, otherwise vertical
    :param length: the length of the ship as an int
    :param fleet: fleet is a list of ship tuple objects e.g. [(row, column, horizontal, length, hits),...]
    :return: returns a boolean True if it is okay to place a ship at a certain location, otherwise False
    """
    result = True

    if horizontal:
        # if horizontal, iterates through ship tiles along the column-axis
        # Ensures that none of the tiles are occupied or adjacent to an occupied tile
        # Otherwise placement is not okay (False).
        for i in range(column, column+length):
            if is_open_sea(row, i, fleet):
                pass
            else:
                result = False
                break
    else:
        # ibid., but for vertical ships.
        for i in range(row, row+length):
            if is_open_sea(i, column, fleet):
                pass
            else:
                result = False
                break

    return result


def place_ship_at(row, column, horizontal, length, fleet):
    """
    Returns an updated fleet with a new ship added.
    A ship is added as a group of tuples, as defined above, but with an empty set 'hits' included.
    :param row: the row number of the tile as an int between 0-9, representing the upper left coord of a ship
    :param column: the column number of the tile as an int between 0-9, representing the upper left coord of a ship
    :param horizontal: a boolean indicating that a ship is placed horizontally if True, otherwise vertical
    :param length: the length of the ship as an int
    :param fleet: fleet is a list of ship tuple objects e.g. [(row, column, horizontal, length, hits),...]
    :return: returns the updated fleet with the new ship added
    """
    hits = set()

    fleet.append((row, column, horizontal, length, hits))

    return fleet


def randomly_place_all_ships():
    """
    Randomly initialises all ships with their positions and type and adds them to a fleet.
    :return: the newly compiled fleet with all 10 ships included
    """
    fleet = []
    # ship_lengths is determined by the fixed number of ships for each ship type in a game.
    ship_lengths = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    # a 'while loop' with a pop() method was preferred as a 'for loop' skipped illegally placed ships
    while len(ship_lengths) > 0:
        row = randint(0, 9)
        column = randint(0, 9)
        horizontal = choice((True, False))
        length = ship_lengths[0]
        if ok_to_place_ship_at(row, column, horizontal, length, fleet):
            place_ship_at(row, column, horizontal, length, fleet)
            ship_lengths.pop(0)  # pop() removes an initialised ship from the list to move onto the next one

    return fleet


def check_if_hits(row, column, fleet):
    """
    Checks if the specified row, column hits a ship by checking if it lies in the list of occupied_tiles for the fleet.
    :param row: the row number of the tile, as an int between 0-9
    :param column: the column number of the tile, as an int between 0-9
    :param fleet: fleet is a list of ship tuple objects e.g. [(row, column, horizontal, length, hits),...]
    :return: boolean True if it is a hit, otherwise False
    """

    if (row, column) in occupied_tiles(fleet):
        return True
    else:
        return False


def hit(row, column, fleet):
    """
    Identifies ship in the fleet that has been hit by a shot, adds the hit to the ship, returns the fleet and the ship
    :param row: the row number of the tile, as an int between 0-9
    :param column: the column number of the tile, as an int between 0-9
    :param fleet: fleet is a list of ship tuple objects e.g. [(row, column, horizontal, length, hits),...]
    :return: the fleet and the ship that's been hit
    """
    ship_hit = ""

    for ship in fleet:

        ship_row = ship[0]  # upper left row coordinate of ship
        ship_column = ship[1]  # upper left column coordinate of ship
        horizontal = ship[2]
        ship_length = ship[3]
        hits = ship[4]

        if horizontal:
            ship_stern_column = ship_column + ship_length - 1  # final column tile of a ship (a stern is a ship's rear)
            if row == ship_row:  # checks that shot is on same row as the ship
                if ship_column <= column <= ship_stern_column:  # checks that shot is within the ship's length
                    ship_hit = ship
                    hits.add((row, column))
        else:
            ship_stern_row = ship_row + ship_length - 1  # final row tile of a ship (a stern is a ship's rear)
            if column == ship_column:  # checks that shot is on same column as the ship
                if ship_row <= row <= ship_stern_row:  # checks that shot is within the ship's length
                    ship_hit = ship
                    hits.add((row, column))

    return fleet, ship_hit


def are_unsunk_ships_left(fleet):
    """
    Returns a boolean True if there are ships remaining in a fleet.
    Returns False if all ships have been sunk.
    :param fleet: fleet is a list of ship tuple objects e.g. [(row, column, horizontal, length, hits),...]
    :return: boolean True if there are ships remaining, otherwise False
    """
    ships_left = False

    for ship in fleet:
        if not is_sunk(ship):
            ships_left = True
            break

    return ships_left


def main():
    """
    Initialises the board. Takes valid user input to determine where to shoot on the board, prints response
    for invalid shots and tracks total number of shots taken. Allows user to quit when correct input is entered.
    """
    current_fleet = randomly_place_all_ships()
    print("Let's play battleships!")
    print("Enter 'quit' to exit the game.")

    game_over = False  # game switch
    shots = 0  # shot counter
    chose_to_quit = False  # game switch if user chooses to quit (returns different end-game message)
    cache_shots = set()  # set of shots which result in a hit

    # for cross-checking user input with numeric pattern to ensure input is valid
    pattern = re.compile("^[+-]?[0-9]+$")

    while not game_over:
        shot_str = input("Enter row and column to shoot (separated by space): ").split()
        # If number of arguments entered is not 2 then the only other valid input is 'quit', otherwise input is invalid
        if len(shot_str) != 2:
            if len(shot_str) == 1 and shot_str[0] == "quit":
                chose_to_quit = True
                break
            else:
                print("Invalid entry, try again!")

        else:
            if pattern.match(str(shot_str[0])) and pattern.match(str(shot_str[1])):  # checks input is numeric
                if 0 <= int(shot_str[0]) <= 9 and 0 <= int(shot_str[1]) <= 9:  # checks input is within bounds
                    current_row = int(shot_str[0])
                    current_column = int(shot_str[1])
                    shots += 1  # if shot is valid, increment shot counter
                    if (current_row, current_column) not in cache_shots:  # checks that tile hasn't already been hit
                        cache_shots.add((current_row, current_column))  # adds new shot to the list of shots
                        if check_if_hits(current_row, current_column, current_fleet):
                            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
                            if is_sunk(ship_hit):
                                print("You have a hit!")
                                print("You sank a " + ship_type(ship_hit) + "!")
                            else:
                                print("You have a hit!")
                        else:
                            print("You missed!")
                    else:
                        print("You've already shot here! Try another tile.")

                else:
                    print("Invalid entry - shot out of range! Try again!")
            else:
                print("Invalid entry, try again!")

        if not are_unsunk_ships_left(current_fleet):  # ends game when all ships are sunk
            game_over = True

    if chose_to_quit:
        print("Finished already? You only took", shots, "shots. See you next time!")
    else:
        print("Game over! You required", shots, "shots.")


if __name__ == '__main__':
    main()

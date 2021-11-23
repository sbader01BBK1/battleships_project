import pytest
from battleships import *

ship1 = (2, 5, True, 1, {(2, 5)})
ship2 = (1, 1, False, 1, set())
ship3 = (4, 8, True, 1, {(4, 8)})
ship4 = (4, 3, False, 2, set())
ship5 = (4, 5, False, 2, {(5, 5), (4, 5)})
ship6 = (8, 6, True, 3, {(8, 7), (8, 8)})
ship7 = (8, 1, True, 4, {(8, 1)})
ship8 = (4, 1, False, 2, set())
ship9 = (0, 8, False, 1, set())
ship10 = (0, 3, False, 3, {(2, 3)})
ship11 = (2, 3, False, 3, {(2, 3), (3, 3), (4, 3)})

fleet1 = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
fleet2 = [ship1, ship3, ship5]
fleet3 = [ship1, ship3, ship6]
fleet4 = [ship2, ship4, ship6, ship8, ship10]
fleet5 = [ship3]
fleet6 = [ship1, ship3, ship5]
fleet7 = [ship3]


# Tests is_sunk for sunk larger ship
def test_is_sunk1():
    assert is_sunk(ship11) == True


# Tests is_sunk for afloat larger ship
def test_is_sunk2():
    assert is_sunk(ship6) == False


# Tests is_sunk for ship with no hits
def test_is_sunk3():
    assert is_sunk(ship4) == False


# Tests is_sunk for afloat larger ship
def test_is_sunk4():
    assert is_sunk(ship10) == False


# Tests is_sunk for sunk small ship
def test_is_sunk5():
    assert is_sunk(ship1) == True


# Tests ship_type for battleship
def test_ship_type1():
    assert ship_type(ship7) == "battleship"


# Tests ship_type for submarine
def test_ship_type2():
    assert ship_type(ship3) == "submarine"


# Tests ship_type for submarine
def test_ship_type3():
    assert ship_type(ship2) == "submarine"


# Tests ship_type for destroyer
def test_ship_type4():
    assert ship_type(ship4) == "destroyer"


# Tests ship_type for cruiser
def test_ship_type5():
    assert ship_type(ship6) == "cruiser"


# Tests occupied_tiles for a 1-ship fleet
def test_occupied_tiles1():
    assert occupied_tiles(fleet5) == [(4, 8)]  # List of board tiles containing a ship


# Tests occupied_tiles for a 3-ship fleet
def test_occupied_tiles2():
    assert occupied_tiles(fleet2) == [(2, 5), (4, 8), (4, 5), (5, 5)]  # List of board tiles containing a ship


# Tests occupied_tiles for a 3-ship fleet
def test_occupied_tiles3():
    assert occupied_tiles(fleet3) == [(2, 5), (4, 8), (8, 6), (8, 7), (8, 8)]  # List of board tiles containing a ship


# Tests occupied_tiles for a 5-ship fleet
def test_occupied_tiles4():
    assert occupied_tiles(fleet4) == [(1, 1), (4, 3), (5, 3), (8, 6), (8, 7), (8, 8), (4, 1),
                                      (5, 1), (0, 3), (1, 3), (2, 3)]  # List of board tiles containing a ship


# Tests occupied_tiles for a 10-ship fleet
def test_occupied_tiles5():
    assert occupied_tiles(fleet1) == [(2, 5), (1, 1), (4, 8), (4, 3), (5, 3), (4, 5), (5, 5), (8, 6), (8, 7), (8, 8),
                                      (8, 1), (8, 2), (8, 3), (8, 4), (4, 1), (5, 1), (0, 8), (0, 3), (1, 3), (2, 3)]
# List of board tiles containing a ship


# Tests is_open_sea for middle of congested board
def test_is_open_sea1():
    assert is_open_sea(4, 5, fleet1) == False


# Tests is_open_sea on edge tile
def test_is_open_sea2():
    assert is_open_sea(0, 0, fleet2) == True


# Tests is_open_sea on occupied tile
def test_is_open_sea3():
    assert is_open_sea(2, 4, fleet1) == False


# Tests is_open_sea on near-empty board
def test_is_open_sea4():
    assert is_open_sea(7, 7, fleet5) == True


# Tests is_open_sea on occupied tile
def test_is_open_sea5():
    assert is_open_sea(3, 3, fleet4) == False


# Tests is_open_sea on edge tile
def test_is_open_sea6():
    assert is_open_sea(9, 9, fleet5) == True


# Tests ok_to_place_ship_at for medium ship horizontally on congested board
def test_ok_to_place_ship_at1():
    assert ok_to_place_ship_at(1, 6, True, 2, fleet1) == False


# Tests ok_to_place_ship_at for large ship vertically on congested board
def test_ok_to_place_ship_at2():
    assert ok_to_place_ship_at(8, 8, False, 4, fleet2) == False


# Tests ok_to_place_ship_at for large ship horizontally over edge of board
def test_ok_to_place_ship_at3():
    assert ok_to_place_ship_at(0, 9, True, 4, fleet5) == False


# Tests ok_to_place_ship_at for small ship vertically on near-empty board
def test_ok_to_place_ship_at4():
    assert ok_to_place_ship_at(2, 2, False, 1, fleet5) == True


# Tests ok_to_place_ship_at for small ship vertically on congested board
def test_ok_to_place_ship_at5():
    assert ok_to_place_ship_at(2, 4, False, 1, fleet1) == False


# Tests ok_to_place_ship_at for small ship vertically over edge of board
def test_ok_to_place_ship_at6():
    assert ok_to_place_ship_at(2, 9, False, 2, fleet2) == False
    # provide at least five tests in total for ok_to_place_ship_at by the project submission deadline


# Tests place_ship_at in existing 3-ship fleet
def test_place_ship_at1():
    assert place_ship_at(0, 8, False, 1, fleet2) == [(2, 5, True, 1, {(2, 5)}), (4, 8, True, 1, {(4, 8)}),
                                                     (4, 5, False, 2, {(5, 5), (4, 5)}), (0, 8, False, 1, set())]


# Tests place_ship_at in existing 3-ship fleet
def test_place_ship_at2():
    assert place_ship_at(8, 1, True, 4, fleet3) == [(2, 5, True, 1, {(2, 5)}), (4, 8, True, 1, {(4, 8)}),
                                                    (8, 6, True, 3, {(8, 7), (8, 8)}), (8, 1, True, 4, set())]


# Tests place_ship_at in existing 5-ship fleet
def test_place_ship_at3():
    assert place_ship_at(6, 7, True, 2, fleet4) == [(1, 1, False, 1, set()), (4, 3, False, 2, set()),
                                                    (8, 6, True, 3, {(8, 7), (8, 8)}), (4, 1, False, 2, set()),
                                                    (0, 3, False, 3, {(2, 3)}), (6, 7, True, 2, set())]


# Tests place_ship_at in existing 1-ship fleet
def test_place_ship_at4():
    assert place_ship_at(0, 0, True, 4, fleet5) == [(4, 8, True, 1, {(4, 8)}), (0, 0, True, 4, set())]


# Tests place_ship_at in existing 10-ship fleet
def test_place_ship_at5():
    assert place_ship_at(6, 7, True, 2, fleet1) == [(2, 5, True, 1, {(2, 5)}), (1, 1, False, 1, set()),
                                                    (4, 8, True, 1, {(4, 8)}), (4, 3, False, 2, set()),
                                                    (4, 5, False, 2, {(5, 5), (4, 5)}),
                                                    (8, 6, True, 3, {(8, 7), (8, 8)}), (8, 1, True, 4, {(8, 1)}),
                                                    (4, 1, False, 2, set()), (0, 8, False, 1, set()),
                                                    (0, 3, False, 3, {(2, 3)}), (6, 7, True, 2, set())]


# Tests check_if_hits in middle of board
def test_check_if_hits1():
    assert check_if_hits(5, 5, fleet1) == True


# Tests check_if_hits on edge of board
def test_check_if_hits2():
    assert check_if_hits(0, 0, fleet1) == False


# Tests check_if_hits outside of board
def test_check_if_hits3():
    assert check_if_hits(12, 12, fleet1) == False


# Tests check_if_hits on ship in board
def test_check_if_hits4():
    assert check_if_hits(8, 8, fleet1) == True


# Tests check_if_hits on ship near edge of board
def test_check_if_hits5():
    assert check_if_hits(1, 1, fleet1) == True
    # provide at least five tests in total for check_if_hits by the project submission deadline


# Tests hit near middle of board on 3-ship fleet
def test_hit1():
    assert hit(4, 8, fleet2) == (fleet2, ship3)


# Tests hit near middle of board on 10-ship fleet
def test_hit2():
    assert hit(8, 3, fleet1) == (fleet1, ship7)


# Tests hit near middle of board on 1-ship fleet
def test_hit3():
    assert hit(4, 8, fleet5) == (fleet5, ship3)


# Tests hit near edge of board on 5-ship fleet
def test_hit4():
    assert hit(2, 3, fleet4) == (fleet4, ship10)


# Tests hit near edge of board on 10-ship fleet
def test_hit5():
    assert hit(2, 5, fleet1) == (fleet1, ship1)


# Tests are_unsunk_ships_left on 10-ship fleet
def test_are_unsunk_ships_left1():
    assert are_unsunk_ships_left(fleet1) == True


# Tests are_unsunk_ships_left on 3-ship fleet
def test_are_unsunk_ships_left2():
    assert are_unsunk_ships_left(fleet6) == False


# Tests are_unsunk_ships_left on 3--ship fleet
def test_are_unsunk_ships_left3():
    assert are_unsunk_ships_left(fleet3) == True


# Tests are_unsunk_ships_left on 5-ship fleet
def test_are_unsunk_ships_left4():
    assert are_unsunk_ships_left(fleet4) == True


# Tests are_unsunk_ships_left on 1-ship fleet
def test_are_unsunk_ships_left5():
    assert are_unsunk_ships_left(fleet7) == False

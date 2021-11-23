 ## BATTLESHIPS
 Completed in partial fulfilment of MSc Computer Science degree at Birkbeck College, University of London
  
 Author: Sam Baderman
 
 The program can be run by cloning this repo, navigating to the directory in the command line and entering
 
 ```
$ python extension.py
```

for the visual version, or

```
$ python battleships.py
```

for the version without visualisation.

 
 ## General idea of the assignment

The Ocean is a field of 10 x 10 squares. The squares are numbered from 0 to 9 in each dimension with numbers increasing from top to bottom and from left to right. 
![ocean](ocean.PNG)

The fleet consists of 10 ships. The fleet is made up of 4 different types of ships, each of different size as follows:

- One battleship, occupying 4 squares
- Two cruisers, each occupying 3 squares
- Three destroyers, each occupying 2 squares
- Four submarines, each occupying 1 square

![ships](battleships.PNG)

To begin the game, the computer places all the 10 ships of the fleet in the ocean randomly. Each ship can be placed either horizontally (as shown in the figure above) or vertically. Moreover, no ships may be immediately adjacent to each other, either horizontally, vertically, or diagonally. Examples of legal and illegal arrangements are shown below:
![legal and illegal arrangements](arrangement.PNG)

The human player does not know where the ships are. The human player tries to hit the ships, by calling out a row and column number. The computer responds with one bit of information--"You have a hit!" or "You missed!" (Note that the human player can call out the same location more than once, even though it does not make sense. If that happens, 2nd, 3rd, ... calls of the same location are misses.) When a ship is hit but not sunk, the program does  **not**  provide any information about what kind of a ship was hit. However, when a ship is hit  _and_  sinks, the program prints out a message  `"You sank a  _ship-type_!"`  

A ship is "sunk" when every square of the ship has been hit. Thus, it takes four hits (in four different places) to sink a battleship, three to sink a cruiser, two for a destroyer, and one for a submarine. The objective is to sink the fleet with as few shots as possible; the best possible score would be 20. (Low scores are better.) When all ships have been sunk, the program prints out a message that the game is over and tells how many shots were required.

## Data Structures

We represent a ship by means of tuples

    (row, column, horizontal, length, hits)

where:

 - `row` and `column` are integers between 0 and 9 identifying, respectively, the row and column of the square of the top-left corner of the ship
 -  `horizontal` is a Boolean value equal to `True` if the ship is placed horizontally and `False` if placed vertically
 - `length` is an integer between 1 and 4 representing the length of the ship
 - `hits` is a set of tuples of the form `(row, column)` containing all the squares occupied by the ship that were hit
 
We represent a fleet by means of a list

    [ship1, ship2, ....]

of ships. Note that during the game,  a fleet will contain 10 ships (which may be intact, hit, or sunk), however, when the computer places the ships randomly, it is convenient to start with an empty list and iteratively expand it by adding ships. 

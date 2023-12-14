inputRaw = """.......#..........................................................................#.........................................................
....................#.........#............#.........................#.......................#..............................................
.#.......................................................#.................#.........................................................#......
..............#.................................#................#....................................................#.....................
..................................#......................................................................#..................................
..................#..................................#.............................#.......#...............................#................
.......#...............................#...................#................................................................................
........................................................................#....................................#........................#.....
..#...........................................................................................................................#.............
............#............#..............................................................................#...................................
...........................................#.....................................................#................#.........................
.....................................................................#...........................................................#..........
...............#....................#.......................................................................................................
#.....................................................#.......................................#............................#..........#.....
.....#................#......#................................................#.............................................................
.......................................#.......................#.......#..............#..................#......#...........................
............................................................................................................................................
...................................................#..............................................#.............................#........#..
..........#........................................................................................................#........................
...............................................#.............................#............#...........#.....................................
....................#..........................................................................................#........#...................
....#.........#............#...............................................................................................................#
....................................#................................#.............#............#...........................................
...............................#..................................................................................#.........................
#...............................................#........#.....................................................................#............
......#........................................................#......................................................#.....................
..........................................#....................................#............................................................
..................#.....................................................................#..................................#.......#........
.............................................................................................#..............................................
.............#........#...........#..........................#............................................#.......#.........................
........#...................#.......................#...................#..................................................................#
.................................................................................#.......................................#..................
................................................................#...........................................................................
...............................................#...........#..........................................#.....#...............................
..........................................#....................................................................................#............
.......#.....#............................................................................#.............................................#...
......................#....................................................#....................................#...........................
.................#...................#................#....................................................................#................
..#...............................................................#...................#.............................#.......................
.............................................................................................#..............................................
.........#..........#.......................................................................................................................
...............................#.........#.......#...............................#.........................................................#
......................................................................................................#...................#.....#...........
........................................................................................#..................#................................
..#.........................................................................................................................................
....................................................................................................................#...................#...
......................#..............................#..........#...........................................................................
......................................................................#..........................................................#..........
#.......................................#......................................................................#............................
.....#..........................#...........................................................................................................
..................#...............................#............................#........................#.................#.................
..........................................................#.................................#...............................................
.......................#..............................................................................................#...........#.....#...
............................................................................................................................................
.......#............................................#.......................................................................................
...............#................#......#......................#......................................#......................................
.....................................................................................#......................................................
............................................................................................................................................
............................................................................................................................................
...#........................................................#...........................#.....#.........................#.........#.........
............................................................................................................................................
...........#..........#......#................................................................................#.............#...............
.......................................#.................................................................................................#..
...............................................#...............#............................................................................
.............................................................................#.....................................#........................
....#..............#..................................................#............#........................................................
..............................#......................#..........................................#.....................................#.....
..............#..........................#...........................................................#......................................
................................................#..............................#..............................#..........#.......#..........
............................................................#...............................................................................
.#........................#.................................................................................................................
...............................#...........................................................#................................................
.............#........................................#........#..................................................#.........................
...........................................#...........................................................#...................#................
.........#.......................................#............................#.......#...................................................#.
.....................................................................#.............................................................#........
...........................................................#................................................................................
.....................................................#......................................#.......#..............#...........#............
............................................................................................................................................
#..........#.....................#..............................................................#........................#..................
...........................#...................#...............................#.....#..................................................#...
................................................................#...........................................................................
.......................................#..................#.......................................................................#.........
...........................................................................................................#................................
......#...............................................#......................#.................#.......................#....................
...............................#..................................#.............................................#....................#......
...........#......................................................................#................#............................#...........
.........................#.........#...............#........................................................................................
.#.........................................#...........................#..................................................................#.
....................#.........................................#.............#...........................................#...................
............................#...................................................................#............................#..............
............................................................................................................................................
.............#..............................................................................#...............#.........................#.....
#......#..........................#...............................................................................#.........................
...............................................#.......................#..................................................................#.
.....................#......................................................................................................................
............................................................#......................#.........................................#......#.......
.........................#............................#................................................................#....................
..#..............................#...............................#..........................................................................
.......................................................................................#.............#..........#...........................
.............#.........................#....................................................................................................
..................................................#...............................#.........................................#...............
...................#..........................................................................#.............................................
.#....................................................#.......#..........................................#......................#.....#.....
...............................#............................................................................................................
..............#....................................................#..........#....................#......................................#.
.........................................................#..............................#..........................#........................
.....#.........................................................................................#.............#..........#...................
..................................#................................................................................................#........
#........................#..................................................................................................................
....................#.......................#................................#..............................................................
...........#.......................................................................#...................#......................#.............
..............................................................#...................................................#.........................
...............................#..................#............................................#............................................
................#.........#.............#............................#....................#................#................................
.#..........................................................................................................................................
........#...................................................................................................................................
..................................#...................................................#.............................................#.......
.................................................................................#..........................................................
.............................#..........................#.....................................#....................#.......................#
........................................#..........................#........................................#...........#.....#.............
......................................................................................................#.....................................
..........#......#.......#....................................................#......................................................#......
.....#...............................................#.................................#........#...........................................
#...........................................#...................................................................................#...........
..............................#..............................#.....................#.......#................................................
......................#.........................#.........................................................................................#.
.......#...........................#.......................................#...............................#............#...................
............#.............................................#........................................#........................................
.....................................................#..............#................#......................................................
............................................................................................................................................
.........................#.................................................................#............#.....................#.............
..................#..........................................................#..................................#......#..................#.
.#.................................................#..........#.........#.........#.........................................................
.......#.........................#.......#..............#..........................................#........................................
.....................#.....#..............................................................................#.................................
...........................................................................#.....................................................#..........
......................................#.........................................................#........................................#..
#...............#...................................#.....................................#............#.................#..................
.............................................#.........................#..........#.............................#...........................
"""

testInputRaw = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

#inputGrid = [[x for x in y] for y in testInputRaw.splitlines()]
inputGrid = [[x for x in y] for y in inputRaw.splitlines()]

# expand rows
i = 0
while i < len(inputGrid):
    if inputGrid[i][0] == '.' and len(set(inputGrid[i])) == 1:
        inputGrid.insert(i, ['Y' for x in range(len(inputGrid[i]))])
        i += 1
    i += 1

# expand columns
i = 0
while i < len(inputGrid[0]):
    colList = [inputGrid[row][i] for row in range(len(inputGrid))]
    if set(colList) == {'.', 'Y'}:
        for rowIdx in range(len(inputGrid)):
            inputGrid[rowIdx].insert(i, 'X')
        i += 1
    i += 1

# # for debugging, print grid
# for row in inputGrid:
#     print(''.join([str(char) for char in row]))

# map galaxy coordinates
expansionAmount = 1000000
galaxyMap = []
curAdjustedY = 0
for y in range(len(inputGrid)):
    if 'Y' in inputGrid[y]:
        curAdjustedY += expansionAmount-2 # subtract 1 for 'X' or 'Y', and one for the dot that should be there instead
    else:
        curAdjustedX = 0
        for x in range(len(inputGrid[0])):
            if inputGrid[y][x] == 'X':
                curAdjustedX += expansionAmount-2
            if inputGrid[y][x] == '#':
                galaxyMap.append((x+curAdjustedX,y+curAdjustedY))

# print(galaxyMap)

# get distances between all pairs
distancesSum = 0
for galaxy1Idx in range(len(galaxyMap)):
    for galaxy2Idx in range(galaxy1Idx+1, len(galaxyMap)):
        galaxy1 = galaxyMap[galaxy1Idx]
        galaxy2 = galaxyMap[galaxy2Idx]
        distancesSum += abs(galaxy2[0]-galaxy1[0]) + abs(galaxy2[1]-galaxy1[1])

print(distancesSum)

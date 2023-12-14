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
        inputGrid.insert(i, inputGrid[i][:])
        i += 1
    i += 1

# expand columns
i = 0
while i < len(inputGrid[0]):
    colList = [inputGrid[row][i] for row in range(len(inputGrid))]
    if colList[0] == '.' and len(set(colList)) == 1:
        for rowIdx in range(len(inputGrid)):
            inputGrid[rowIdx].insert(i, '.')
        i += 1
    i += 1

# map galaxy coordinates
galaxyMap = []
for y in range(len(inputGrid)):
    for x in range(len(inputGrid[0])):
        if inputGrid[y][x] == '#':
            galaxyMap.append((x,y))

# get distances between all pairs
distancesSum = 0
for galaxy1Idx in range(len(galaxyMap)):
    for galaxy2Idx in range(galaxy1Idx+1, len(galaxyMap)):
        galaxy1 = galaxyMap[galaxy1Idx]
        galaxy2 = galaxyMap[galaxy2Idx]
        distancesSum += abs(galaxy2[0]-galaxy1[0]) + abs(galaxy2[1]-galaxy1[1])

print(distancesSum)
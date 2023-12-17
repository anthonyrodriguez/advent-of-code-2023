inputRaw = """...OO..##.......O..O....O..O#...O.OO#.#..O...O....OOO##..O##O#...#..O....#........#O.##O#..OO#..OO.O
...#.#.#.O#...OO.#........O#.#............#...O...#...OOOO#...#..#..#.O...#..#....O.#O###..O#..OOO.O
..##..##.O...#..OO.O.#.#O#.O.OO..#.....#.....#O##O.#..###.O.........OOOO#...O.#.........##O..O.#O.O.
.....#.##O##.#.#O#....#.#O.....OO.#.#OO##OOOO..#O..#.#.#.O..........O.#......O...OO.........#.OO....
.#.O#O...#...#...O#O....O.......O#.O..OOO...#.##OO.#.O..O.#.O...O..O.#.#.#...#..O...OO..OO.....O.#.O
....#..#...#.##................O..OO.....##.........#...#..........#.OOO...O#..##.##.......#O..O.##.
.............OO#...O.#....O....O...##...OOO....O.O..O...#......O..O#.O#.#..........#.#....#O...#O..O
O.....O.O...O...OO..#...#.OO........#..##O...O.O.#.#..#O..##O.##..O......#.....O......#....O.....OO.
.#..O....O.O..O.#..#.......#OOO...#.O..O..O#...OO.#...##O.O..O.OO...O....#O.O.....O#....O....O.#....
...#....#OO...O....#.##.O#####..O...#...#...#..O..#.##.##OO...O#.........O..OO......#..OO.#...##O...
...OO...........O....O.##..#.O##.....O..#.......O#..#....#O.#...#.#.O..O#..#..O..O##..O...#..O##.O..
.....#OO#.O......#.O..O..O.....#.#.OOOOO..#......O.OO.OO.....#...#O....OO.O.#....##O..O..O......#...
.O#O.#.#O.....O.#..O..#O..#O.O..O.......O....O.....#...#........#.#....O#..#......#O....OO#.....O.##
.O..###.....O..##O...O..O..O.#....#.......#..##......O#O.#OOO...OOO...O..O#..#.#...OOO#..........O..
#..O#OO..#O.O..OOO...#.#...O..O.O.......#..#...#..O...O.O#.O....#...#..O.O....O.#.#...#.....OO...#.#
...O..#O............#.......#..##OO..##....#OO.OO..##..#OO.#.O..O.O........O........O.##...O.O.O...#
.O...O.....#....OO#.O#.###.O....#.O...O#....#....O....O..OO.O....O#OO#.#O#......OO..OOO...O.#.O.....
.O..O................OO##O..#....O..#.O..#.#............#.##.........#..O.O.O..O#...O.#OOO#..#.#...#
O..O.........O##...#......#..#O....#O#....O.O.O.O...#......O#O..#...O..##.#..O.O.#O.......OO...O#O##
OOOO.#O.O#.....#..#...#..O...#O....#.#.O.#..O.##.O....#.##.O.O....OO...O.......#..#......#...O###..O
..#.......#...O..O..OO.O#...OO.OO..O#.O....#OO....#.#O........##O.#.....###....OO#..O.O.O.......O#.#
#.O.......#OO#...#O#O#..OO.O.OOO#O#....OO..O#.O.#.O...##.#.O..#...O.O.....O..#.OO#.O...O.#....O.O..#
.OO#.OO###....O........#..O..##.O...OOO.#...O......O#....#.O#.O......O.......O.#..#O..O...#..#...#..
....##O....O.##......##.O.##......#....OOOOO#......#.#.....#O...#...#..OO##.##.....##.O...O.O##.#..O
.#...O.#OO........O..OO...##O.O..O.....O..#OOO....#..#O#.#O......O.O.##.....O......O.O.#..#.#..OO...
O...O....#...O##.....#......O.O..O..O..#...O..OO#..O#.#.....#....O...##.#.#O.O........#.O#O#OO.#..#.
#..#...#OO...O#..#.#.#O#O..........O..O...O.O#O...OOO..O...O.O#.O##....O.......O..O..#...OO..OOO....
.#.OOO#....O#.....#.OOO.........O.........O.......#O#O......O#O.O.#O#.#..O.....#.....#..O.##O.O#...#
...#....O.O##.O...O.O..OOOO##.............OO....O.O....O..O....#OO..O....OO.OO.O..#.#......O.O#.....
#....O...OO.#.....O...OO.#O.#O....#....##.O..#O..O.O...#...O#.#OOOOOO......#.O.##......##..###.O.O..
.#.O..O.##O.#.........O.O.#O....#......O.#....O...#O.#.OO.OOO..#..O.O.##..#.....#..O.....O#..O#....O
#.OO.#...O...O##O.O.O......#....O..O.O.......O.....#...OOO....O.O#.#..O.O..OO#.OOO..O...#..O..O.OO.#
.#..#........##O.O.....OO.....O...OO#O..#..O.....O...O....O.#.#.......OO.....O..O.O..O....#.#O.....#
...O.O.OO.O##OO..O.OO.......#O#O#..O#...O.#O.....#.....#.OO.#..#....O..OO.O.....O....O..#.OO.......O
O#..........O.#..OO...#OOO.O..O.##..#O##O.O.#O#.OO.O.O#...O#...OOO#.O.OO.O.#O..#O.#.......##O..O...O
.#.O.....#..O#....O.###.....##...O.....................O....OO#..O#.#.#...O....##...O.#...O..#.O##.#
..O...#...O#.#.O.O.O...O.......OO#.#........O...##.O...#..##..OO.#..O.#.#.O..OO....O.O..#...#O.O#.#.
....OOO#.O#...#...O#.O.OOO...##.....O...OO...O..OOO.O.O.O..##.#O#.#O.O...#O..O..#.#..OOOO..O.#.O#...
.O............#....#..OO...#..OO.OO....O..O.OOO......O....O#OO....#............#.OO#.O##.O#O..OOO.#O
.O......O.#.#.#..O.......O.........#O.O...#O#...#.OO...#...#.O..O..O.O.#.O.O.....#.#......##.O.O...O
...O..O.........#O..O.O..O###O#..#..#OO#OO..#O.#.....##..OO...OOO#...#O.........OOO.OO.##..#O.O..O.O
.#.##.#.#OOO#.OO.O.O#OO#O....O..#...O.......O.#.....##...#O..O.O...#..##O......OO.OOO..O...#.#.O#O..
.#.O##O#...#.O.#O..OO##....##O................#..#..#..#.O....#....#.#.#..#O..#...O.#O..#...O...OO..
.....O.......O##......OO..#...O...#.O..O..O#.O..##..#.O..#....#.O.#O....O..OO.#OO.#..#...#.O...OO.O.
..#O.###...O..###O..#..#....OO...O.O....O.#O#.#O..O..O..#..#..#....#..O.OOO...O.#O.....O..O....O.OO.
.O#....O.##O..........O.#OO..O...O...#..##.OO...#.#..OO.O.....##O..OO...O...OOO..#.#....OO..#OO.O...
O....O.#O#O....OO.......O..O.O.....O...#.O..#.OO..OO.....#....O...OO.##...O.....#O..O...O##.O.#O...#
O...#..O....#.O.O..O#.....O..#.OO#O#OO##O##...O.O.....O...#...O...OOO...O#O...O.#OO.##..O..##O.O#...
.#O..#O#..#.#........O..O#.......#...O.....O....O...O#..#.#..#...#.....#...#.#.....OO...O.##O.......
O#........O#...O.O.##...O.OOO.........##..........#O#............O...O.#O.O#.#.#.#.O..#....#........
.........#.#......##OOO....O.#O....OO..O....O.##....#......O.O........#O..#.O....##.........#.O.#...
#.#.O..O....OO#......#.O#....#O..OO..O.....O..#.#O#.O.##O....O......#O......OOO....#O.#OO....O.O..##
OO.O.##O.....O#....O.O#....O..###.O.O...O..#...O..#O....O..#OO...O...##.....O.#OO.....O...#O.O..#..O
.OOO#...O..#O..O......OOO..O..O...#.O.O#...OO.......O.O.O##...#O..O.......##....O#.OO###.....O...O.O
.O..O...#O.#....##.O.O.O.#......O.O.#.O#.O###....O...O..#..O#......O.........OO...OOO..#.O.....O....
.O...##...O#.........O..O.O....O...#..#.....O.#..O.#O..O.#.O....#..O..#....#.#.OOO...O#...#O#.#O..#.
#.#........O#.#.O.O.#.#.OOO.#.#.#O.#....#O.#.O..#..........#O..O#.##..O#O#.O.OOO..##..O....O.#.OO...
O..O..O.........#OO.#....#....O..O#O..O#....O..O.O.........O............OOOO..OO#.O#......O..#.#..#.
#..O.....#........O.....O....O#O##..O.O...##..#O.#.OO..#......#.#..O.......#....O..O.....#..O.....O.
..O.#.##...O..##O.....#..........O........#.#.#O..O.OO..OO.....O.....O..OO..OOO.#.#.O#.....#.#..O#.#
.................O...O.#.....#...O#....OO..#O...O....OO.OOO.##..##..O........#O#O..#....#.....#....#
..#.#..O....##.#O.....#.OOO.O.O....O#..O....OO......O.#.O#...#.#.O...O....#.......#O.O.#O.O.##.##.#O
..O..O.....#O........#O....#.#.........O.#....O..O.#.O...O#.O.#......O...O..#.......#O....##...##...
....OO.#......O...O#...#....##.#.O..#.O#.O#..O#....##.O#...O..O.....#.#..#O.#.....##O#.O#..O.O....#.
#..O..#..........#..O##O....#.#..O#...O..O.##.....OO..#...##O..####....O.......#........O.O....O.O..
.#.OO#.O.O...#OO.O#.O.#.#....O..#...OO..O.....#O.....#..##...O..###OO..O....#..O#..#O...O..O..#O...#
#..#OO#..O#.....#O..O.O.O...#.O..OO.O.O#..#....#O..O.OO........##..O......O#...OO#...#.....OO..#.#..
.#.##.O.O..O.....OOO..OOO..#..OO#...##.O.O.#..#..O.....O#...O.#...O.......O#.#.#O#...O..#...##...O..
.#..O..#.O.##O..O#.O.O....#.##....#.OO#.....##..OO#.#O.#.#...O#....OOOOO...O#.....##......O.........
.....###......#O...OO..O#.O.....O.#O.....#O##.#.##..#..#O..OO##..O...OO..O####O....O...O..O.#.O#.#..
.O#..O.O.O...#O..#..#....###..##...O.OOO.....O.#..O#.O.OO.O..O#...#.O...#.O#.O#.....#.OO..OO#..OO.O.
#....O#...#.......O........#....O##.O#......O........O#.O...OO...O#.#.O...OO..O............OO...OO.#
#.##...#O..OO...#.....#.O..O.O....O..O.....#O.OO.O...O.O.OO.##.O......#O.#.#O.#.O....O.OOO...O#O..O.
..#.#OOO.O...#..O.O#O.O...#.#..........#.O.##.O.##.O....###.#.#...#.O........#...#.O......O..#.OO...
OOO......##.....#....O......O.....#O#O...O......OOO.O.O....OO##O#.OOO#..O..O.#.#...O....#.O.O..O..##
.....O.#....#.##O.OOO.O.....O.#O..#O...#....OO.#..#.O..OO.O.##...O#...O.O##.O......O.#..O#O.OOO....O
#O..#...#..O...O.O.O...#..OOO..O.O..#...#.#..O.O#...O.......OO...O.##O...O#.....O.O....O..O.O.#.#O..
..O...#...O#......O....OO...#.#..#.O...#...O.O...O.O.......O....O...O..#....O...O.....##..O.#...#.#.
.#....#O#OO...O....##.#.O.O...O#........##.O.#...OO...O#.....O.......O.O.O##....#..OOO..........#...
...#..O....O#......O...##O.#.O.O.OO.O.#......##.O..O......O..O.#..O....O.....#O##...#.#O.OO.#O#.###.
#...#...#O.....#...O###......O#O..O.O.....O....O....#O....O#..#.O..OO###....O...O#......O.#O#....O..
#.....#OOO##.....O...#.O.##O..##.O......#OO.O..#.........O#.O.#.O....O#OO.O.OO..O##O#.......O.....O.
.#..#..#O.OOO.#...###.O...#..OO#.OOO#................O...O.O.........O.....#...#O.OO...O...#O.#..O.#
.O#O..#.#O....O..O.#.....O....#.O#O.O...#.OO..O.#........#...O...O.O....O#O......OOO.O.....O#.#O..O.
#.#.O#..O...#O..#....O.........O....##...#.#..#.O.#OO...O...O.#...#.....O#..O#.O#.O..OOO.O....O..O..
O..O.......#O#O.O......O.O....O#OOO.....##O....#.##..#.OOOO....#..O....#...#.O...#O.....#O#O..O..#..
..#...O.#.O#.O.O#.O....#.#....#.#...O.#O.##..O.#.....O...#...#....O.#..O#..#.#OOO#..OO.#.#O.#..O#..#
.OO.O..#.#..#.#..#O.O....#O..#O.......#.#.O.#.#.#.##..#.#O.#.O..#.O...O.#..#...O..O......##.......O.
...O.O..O.O.O.#.O#.O......O.O#.O#....OO......#O.#.O......O.OO.#O....O#........#..#..O.O#.#O#O..#...#
...#..O....#OO.OO#.OO.#.....OOO.OO##OO#......O....O......#O#.#.O..O....O..O.O..#O...#......#........
......#.....O#.O..#..O......O##.#.O........##.##...OOOO..#...#.O...#..OO.O.#.#.O.#...#.#OO#O....##..
.OO....#...O.#....O......#.O....O.....#.O..O.#.O....O.O#OO.O.O.#............#.#O#..##O..O.#..#.O##..
#.O#..#.#O..OO#O.O##..O...#.#O.....O..O.##....#.#...O.O....O.#...O..O#.#.OO..OOO..O..O.O.#..OO#...#.
....#.O..OO..O.##.O.#O..O.O.O..#..#.O.O....###O..#OO#....#.........O.###.O...O#.O...O#.#.O#O.O#OO.O.
O.#......O...OO.#.#.O..#.O............O#.O#O........#..O.#O#.#.#..O.OO..#.OO#.O.#.#O###..##..##.....
..O#O....O...#....................O#..#.O.#....O.#OOO...O.OOO.#..#..O##.O...O.....O.#.OO.....O..#..#
#.O....##O..##...#.#.OO...#.......#.#........#####.O.O......##.....#...........O#OO.O..#....O...O#..
..........#.O.#.#.#OOO.O..O.O.O.#O...#..O#....O..O##.O..#O...OO#O..OOO..OO#O#.O.....O..O##.O...#....
O###...O#.O......##O#..O#.........OO...O#O#O..#O#O..#O#O.#..#OO.#...##..##..#.#...#O.O....O...O....#
.#.....O#OO.O#.#.OOO#.#.#.#...O.#..##.##...O.OO.O.....O..##..O.......O..#...O....##OO#..O#.OOO.#.##.
"""

testInputRaw = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

#platformArr = [[char for char in row] for row in testInputRaw.splitlines()]
platformArr = [[char for char in row] for row in inputRaw.splitlines()]


def printPlatform(platform):
    for row in platform:
        print(''.join(row))
    print()


def tiltPlatformNorth(platform):
    tiltedPlatform = [row[:] for row in platform[:]]
    for colIdx in range(len(platform[0])):
        blockerIdx = 0
        roundRockCount = 0
        for rowIdx in range(len(platform)):
            if platform[rowIdx][colIdx] == 'O':
                roundRockCount += 1
            if platform[rowIdx][colIdx] == '#':
                for tiltRowIdx in range(blockerIdx, blockerIdx + roundRockCount):
                    tiltedPlatform[tiltRowIdx][colIdx] = 'O'
                for emptyRowIdx in range(blockerIdx + roundRockCount, rowIdx):
                    tiltedPlatform[emptyRowIdx][colIdx] = '.'
                blockerIdx = rowIdx + 1
                roundRockCount = 0
        # Tilt up rocks again til the end of the col
        if roundRockCount > 0:
            for tiltRowIdx in range(blockerIdx, blockerIdx + roundRockCount):
                tiltedPlatform[tiltRowIdx][colIdx] = 'O'
            for emptyRowIdx in range(blockerIdx + roundRockCount, len(platform)):
                tiltedPlatform[emptyRowIdx][colIdx] = '.'

    return tiltedPlatform


def getNorthLoad(platform):
    totalLoad = 0
    for rowIdx in range(len(platform)):
        loadMultiplier = len(platform) - rowIdx
        totalLoad += platform[rowIdx].count('O') * loadMultiplier
    return totalLoad


def rotateClockwise(platform):
    return [list(reversed(col)) for col in zip(*platform)]


def runTiltCycle(platform):
    # tilt north and rotate a total of 4 times (to end back at north but not tilted)
    for i in range(4):
        platform = tiltPlatformNorth(platform)
        platform = rotateClockwise(platform)
    return platform

def hashPlatform(platform):
    return ''.join([char for row in platform for char in row])


def findTiltCycleLoop(platform):
    platformStateHashes = {}
    curCycle = 0
    for i in range(1000000000):
        platform = runTiltCycle(platform)
        curCycle += 1
        hashedPlatform = hashPlatform(platform)
        if hashedPlatform in platformStateHashes.keys():
            # Tilted platform, length of loop, loop start
            return (platform, curCycle-platformStateHashes[hashedPlatform], platformStateHashes[hashedPlatform])
        else:
            platformStateHashes[hashedPlatform] = curCycle


# for i in range(1000000000):
#     platformArr = runTiltCycle(platformArr)
# print(getNorthLoad(platformArr))

platformArr, tiltCycleLen, tiltCycleStart = findTiltCycleLoop(platformArr)

remainingCycles = (1000000000 - tiltCycleStart) % tiltCycleLen

for i in range(remainingCycles):
    platformArr = runTiltCycle(platformArr)
print(getNorthLoad(platformArr))


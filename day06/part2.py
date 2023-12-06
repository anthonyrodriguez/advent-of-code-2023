testInputRaw = """71530
940200
"""

inputRaw = """40817772
219101213651089
"""

#inputListRaw = testInputRaw.splitlines()
inputListRaw = inputRaw.splitlines()

[raceTime, raceDist] = [int(x) for x in inputListRaw]

firstWayToWin = 0
lastWayToWin = 0

for timePressed in range(raceTime):
    if timePressed * (raceTime - timePressed) > raceDist:
        firstWayToWin = timePressed
        break

for timePressed in range(raceTime, 0, -1):
    if timePressed * (raceTime - timePressed) > raceDist:
        lastWayToWin = timePressed
        break

# plus one because it's inclusive of both ways to win
print(lastWayToWin - firstWayToWin + 1)

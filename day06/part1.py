testInputRaw = """Time:      7  15   30
Distance:  9  40  200
"""

inputRaw = """Time:        40     81     77     72
Distance:   219   1012   1365   1089
"""

#inputListRaw = testInputRaw.splitlines()
inputListRaw = inputRaw.splitlines()

[timeList, distList] = [[int(x) for x in y.split(' ') if str.isdigit(x)] for y in inputListRaw]

waysToWinList = []

for i in range(len(timeList)):
    waysToWin = 0
    totalRaceTime = timeList[i]
    for timePressed in range(totalRaceTime):
        if timePressed * (totalRaceTime - timePressed) > distList[i]:
            waysToWin += 1
    waysToWinList.append(waysToWin)

print(waysToWinList)

waysToWinProduct = 1
for win in waysToWinList:
    waysToWinProduct *= win
print(waysToWinProduct)

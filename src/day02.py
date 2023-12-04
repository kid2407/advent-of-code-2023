import time
from typing import Tuple, Dict, List

from InputHelper import InputHelper

helper = InputHelper(2)
data = helper.load_data()


def parseLine(line: str) -> Tuple[int, List[Dict[str, int]]]:
    gameString, dataString = line.split(": ")
    gameNumber = int(gameString.split(" ")[1])

    dictList = []

    for section in dataString.split("; "):
        dataDict = {"red": 0, "blue": 0, "green": 0}
        for draw in section.split(", "):
            amount, color = draw.split(" ")
            dataDict[color] = int(amount)
        dictList.append(dataDict)

    return gameNumber, dictList


def isValidGame(amountRed: int, amountBlue: int, amountGreen: int, gameList: List[Dict[str, int]]) -> bool:
    for draw in gameList:
        if draw["red"] > amountRed or draw["blue"] > amountBlue or draw["green"] > amountGreen:
            return False

    return True


def getPowerForGame(gameList: List[Dict[str, int]]) -> int:
    minCountRed = 0
    minCountBlue = 0
    minCountGreen = 0

    for draw in gameList:
        if draw["red"] > minCountRed:
            minCountRed = draw["red"]
        if draw["blue"] > minCountBlue:
            minCountBlue = draw["blue"]
        if draw["green"] > minCountGreen:
            minCountGreen = draw["green"]

    return minCountRed * minCountBlue * minCountGreen


start = time.time()
sumPossibleGameIDs = 0
for game in data:
    gameId, gameData = parseLine(game)
    if isValidGame(12, 14, 13, gameData):
        sumPossibleGameIDs += gameId

print("The the sum of valid game IDs is {}, calculated in {:.2f}ms".format(sumPossibleGameIDs, (time.time() - start) * 1000))

start = time.time()
sumOfPowers = 0
for game in data:
    gameId, gameData = parseLine(game)
    sumOfPowers += getPowerForGame(gameData)

print("The sum of the game powers is {}, calculated in {:.2f}ms".format(sumOfPowers, (time.time() - start) * 1000))

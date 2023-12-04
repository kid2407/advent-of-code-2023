import time

from InputHelper import InputHelper

helper = InputHelper(1)
data = helper.load_data()


def sumCalibrationValues(lines: list[str]) -> int:
    calibrationValuesSum = 0
    for line in lines:
        firstDigit = None
        lastDigit = None

        for character in line:
            if character.isdigit():
                if firstDigit is None:
                    firstDigit = int(character)
                lastDigit = int(character)
        calibrationValuesSum += firstDigit * 10 + lastDigit
    return calibrationValuesSum


def sumRealCalibrationValues(lines: list[str]) -> int:
    digitsAsWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    trueCalibrationValuesSum = 0
    for line in lines:
        firstDigit = None
        lastDigit = None

        for currentIndex, character in enumerate(line):
            if character.isdigit():
                if firstDigit is None:
                    firstDigit = int(character)
                lastDigit = int(character)
            else:
                for i, word in enumerate(digitsAsWords):
                    if line[currentIndex:].startswith(word):
                        if firstDigit is None:
                            firstDigit = i + 1
                        lastDigit = i + 1
        trueCalibrationValuesSum += firstDigit * 10 + lastDigit
    return trueCalibrationValuesSum


start = time.time()
task1Sum = sumCalibrationValues(data)

print("The sum of the calibration values is {}, calculated in {:.2f}ms".format(task1Sum, (time.time() - start) * 1000))

start = time.time()
task2Sum = sumRealCalibrationValues(data)

print("The real sum of the calibration values is {}, calculated in {:.2f}ms".format(task2Sum, (time.time() - start) * 1000))

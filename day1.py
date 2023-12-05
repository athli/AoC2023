import regex as re

def calibrationNumbers(filename):
    sum = 0
    with open(filename) as f:
        for line in f:
            numList = re.findall(r'\d', line)
            if len(numList) != 0:
                num = numList[0] + numList[-1]
                sum += int(num)
    return sum

def calibrationNumbersAndWords(filename):
    sum = 0
    wordToInt = {
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    with open(filename) as f:
        for line in f:
            numList = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
            if len(numList) == 0:
                continue
            elif len(numList) == 1:
                if numList[0] in wordToInt.keys():
                    sum += int(wordToInt[numList[0]] + wordToInt[numList[0]])
                else: sum += int(numList[0] + numList[0])
            else:
                num = ''
                if numList[0] in wordToInt.keys():
                    num += wordToInt[numList[0]]
                else: num += numList[0]
                if numList[-1] in wordToInt.keys():
                    num += wordToInt[numList[-1]]
                else: num += numList[-1]
                sum += int(num)
    return sum

print(calibrationNumbersAndWords("day1input.txt"))
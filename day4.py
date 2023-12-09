def totalPoints(filename):
    sum = 0
    with open(filename) as f:
        for line in f:
            nums = line.split(':')[1]
            winners = nums.split('|')[0]
            mynums = nums.split('|')[1]
            winningList = [int(x) for x in winners.split()]
            myList = [int(x) for x in mynums.split()]
            matches = 0
            for num in myList:
                if num in winningList:
                    matches += 1
            if matches != 0:
                sum += 2 ** (matches - 1)
    return sum

def matchesPerLine(line):
    nums = line.split(':')[1]
    winners = nums.split('|')[0]
    mynums = nums.split('|')[1]
    winningList = [int(x) for x in winners.split()]
    myList = [int(x) for x in mynums.split()]
    matches = 0
    for num in myList:
        if num in winningList:
            matches += 1
    return matches

def allThePoints(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    cardCount = [1]*(len(lines))
    for i in range(len(lines)):
        matches = matchesPerLine(lines[i])
        for j in range(matches):
            cardCount[i+j+1] = cardCount[i+j+1] + cardCount[i]
    return sum(cardCount)

print(allThePoints('day4input.txt'))
def waysToWin(filename):
    f = open(filename)
    time = int(f.readline().split(':')[1].replace(' ',''))
    distance = int(f.readline().split(':')[1].replace(' ',''))
    f.close()
    result = 0
    for j in range(time):
        if j * (time - j) > distance:
            result += 1
    return result

print(waysToWin("day6input.txt"))
def waysToWin(filename):
    f = open(filename)
    times = f.readline().split()[1:]
    distances = f.readline().split()[1:]
    f.close()
    races = len(times)
    result = 0
    for i in range(races):
        wins = 0
        time = int(times[i])
        distance = int(distances[i])
        for j in range(time):
            if j * (time - j) > distance:
                wins += 1
        if wins != 0:
            if result == 0:
                result = wins
            else: result *= wins
    return result

print(waysToWin("day6input.txt"))
def validGames(filename):
    # r <= 12, g <= 13, b <= 14
    sum = 0
    with open(filename) as f:
        for line in f:
            game = int(line.split(':')[0].split()[1])
            handfuls = line.split(':')[1].split(';')
            flag = False
            for handful in handfuls:
                colors = handful.split(',')
                for color in colors:
                    if 'red' in color and int(color.split()[0]) > 12:
                        flag = True
                        break
                    if 'green' in color and int(color.split()[0]) > 13:
                        flag = True
                        break
                    if 'blue' in color and int(color.split()[0]) > 14:
                        flag = True
                        break
            if flag: continue
            else: sum += game
    return sum

def powerofGames(filename):
    sum = 0
    with open(filename) as f:
        for line in f:
            handfuls = line.split(':')[1].split(';')
            r = 1
            g = 1
            b = 1
            for handful in handfuls:
                colors = handful.split(',')
                for color in colors:
                    if 'red' in color and int(color.split()[0]) > r:
                        r = int(color.split()[0])
                    elif 'green' in color and int(color.split()[0]) > g:
                        g = int(color.split()[0])
                    elif 'blue' in color and int(color.split()[0]) > b:
                        b = int(color.split()[0])
            power = r*g*b
            sum += power
    return sum

print(powerofGames("day2input.txt"))
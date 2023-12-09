import re

def sumOfParts(filename):
    sum = 0
    f = open(filename)
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        for match in re.finditer(r'\d+', lines[i]):
            start = min(match.start(), abs(match.start() - 1))
            end = min(match.end() + 1, len(lines[i]))
            top = min(i, abs(i - 1))
            bottom = min(i + 2, len(lines))
            for j in range(top, bottom):
                if re.search(r'[^\d\.]', lines[j][start:end]) is not None:
                    sum += int(match.group())
                    break
    return sum 

def sumOfGears(filename):
    sum = 0
    f = open(filename)
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        top = min(i, abs(i - 1))
        bottom = min(i + 2, len(lines))
        for match in re.finditer(r'\*', lines[i]):
            start = min(match.start(), abs(match.start() - 1))
            end = min(match.end() + 1, len(lines[i]))
            parts = []
            for j in range(top, bottom):
                for m in re.finditer(r'\d+', lines[j][start:end]):
                    partNum = re.findall(rf'\d*{m.group()}\d*',lines[j][max(0,match.start() + m.end()-4):min(match.start() + m.start()+2,len(lines[j]))])
                    if len(partNum) != 0:
                        for k in range(len(partNum)):
                            partNum[k] = int(partNum[k])
                        parts += [max(partNum)]
            if len(parts) == 2:
                sum += (parts[0] * parts[1])
                print(parts)
    return sum 

print(sumOfGears('day3input.txt'))
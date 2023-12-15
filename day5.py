import re

def seeds_to_location(filename):
    location = 0
    with open(filename) as f:
        input = []
        output = []
        for line in f:
            if "seeds:" in line:
                seedrange = [int(z) for z in line.split()[1:]]
                for i in range(len(seedrange)):
                    if i % 2 == 1:
                        for j in range(seedrange[i]):
                            input.append(seedrange[i-1] + j)
                output = [-1] * len(input)
                continue
            elif ":" in line and output != [-1]*len(input):
                for i in range(len(input)):
                    if output[i] == -1:
                        output[i] = input[i]
                input = output
                output = [-1]*len(input)
            elif re.match(r'\d', line) is not None:
                vals = [int(x) for x in line.split()]
                offset = vals[0]-vals[1]
                for i in range(len(input)):
                    if (vals[1] <= input[i] and input[i] < (vals[1] + vals[2])):
                        output[i] = input[i] + offset
    for i in range(len(input)):
        if output[i] == -1:
            output[i] = input[i]
        location = min(output)
    return location

print(seeds_to_location('day5input.txt'))
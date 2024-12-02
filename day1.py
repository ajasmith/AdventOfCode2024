def open_file(path):
    with open(path, "r") as file:
        data = file.readlines()
        return data

def parse(path):
    lines = open(path)
    data = list(map(str.split, lines))
    c1 = list(map(lambda x: int(x[0]), data))
    c2 = list(map(lambda x: int(x[1]), data))
    return (c1, c2)

def run_part1(path):
    c1, c2 = parse(path)
    c1.sort()
    c2.sort()

    total = 0
    for x in zip(c1,c2):
        diff = abs(x[1]-x[0])
        total += diff

    return total

def run_part2(path):
    c1, c2 = parse(path)
    c2.sort()
    
    prev = -1
    counts = {}
    for i in c2:
        if i == prev:
            counts[i] = counts[i] + 1
        else:
            counts[i] = 1
            prev = i

    score = 0
    
    for i in c1:
        if (i in counts):
            score += counts[i] * i

    return score    

print(run_part1("data/day1_test.txt"))
print(run_part1("data/day1.txt"))
print(run_part2("data/day1_test.txt"))
print(run_part2("data/day1.txt"))

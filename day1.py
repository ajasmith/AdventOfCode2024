import helpers

def parse(path):
    data = helpers.parse_to_int_lists(path)
    c1 = list(map(lambda x: x[0], data))
    c2 = list(map(lambda x: x[1], data))
    return (c1, c2)

def part1(path):
    c1, c2 = parse(path)
    c1.sort()
    c2.sort()

    total = 0
    for x in zip(c1,c2):
        diff = abs(x[1]-x[0])
        total += diff

    return total

def part2(path):
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

print(part1("test/day1.txt"))
print(part1("data/day1.txt"))
print(part2("test/day1.txt"))
print(part2("data/day1.txt"))
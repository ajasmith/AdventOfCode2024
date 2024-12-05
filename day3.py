import helpers
import re

def run(path, search):
    total = 0
    active = True
    for line in helpers.open_file(path):
        results = re.findall(search, line)
        for p in results:
            if (len(p) > 2):
                if (p[2] == r'do'):
                    active = True
                    continue
                if (p[2] == r"don't"):
                    active = False
                    continue
            if (active):
                total += int(p[0]) * int(p[1])
    return total

def part1(path):
    return run(path, r"mul\((\d+),(\d+)\)")

def part2(path):
    return run(path, r"mul\((\d+),(\d+)\)|(do(?:n't)?)\(\)")

print(part1("test/day3.txt"))
print(part1("data/day3.txt"))
print(part2("test/day3.txt"))
print(part2("data/day3.txt"))
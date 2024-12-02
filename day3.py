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

def run_part1(path):
    print(run(path, r"mul\((\d+),(\d+)\)"))

def run_part2(path):
    print(run(path, r"mul\((\d+),(\d+)\)|(do(?:n't)?)\(\)"))

run_part1("test_data/day3.txt")
run_part1("data/day3.txt")
run_part2("test_data/day3.txt")
run_part2("data/day3.txt")
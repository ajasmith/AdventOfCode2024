import helpers
import re

def run_part1(path):
    search = r"mul\((\d+),(\d+)\)"
    total = 0
    for line in helpers.open_file(path):
        results = re.findall(search, line)
        for p in results:
            total += int(p[0]) * int(p[1])
    print(total)

def run_part2(path):
    search = r"mul\((\d+),(\d+)\)|(d)o\(\)|do(n)\'t\(\)"
    total = 0
    active = True
    for line in helpers.open_file(path):
        results = re.findall(search, line)
        for p in results:
            if (p[2] == "d"):
                active = True
                continue
            if (p[3] == "n"):
                active = False
                continue
            if (active):
                total += int(p[0]) * int(p[1])
    print(total)

run_part1("test_data/day3.txt")
run_part1("data/day3.txt")
run_part2("test_data/day3.txt")
run_part2("data/day3.txt")
from math import floor, log
import helpers

seen = {}

def n_digits(x):
    return 1 if x == 0 else floor(log(x, 10)) + 1

def split(stone):
    s = str(stone)
    mid = int(len(s)/2)
    return [int(s[0:mid]), int(s[mid:len(s)])]

def blink(stone):
    if (stone == 0):
        return [1]
    elif (n_digits(stone) % 2 == 0):
        return split(stone)
    else:
        return [stone * 2024]

def count_stones(stone, nblink):
    if (stone, nblink) in seen:
        return seen[(stone, nblink)]
    elif (nblink == 0):
        return 1
    else:
        next = blink(stone)
        result = 0
        for s in next:
            result += count_stones(s, nblink-1)
        seen[(stone, nblink)] = result
        return result
    
def calc(stones, nblinks):
    count = 0
    for s in stones:
        count += count_stones(s, nblinks)
    return count

def run(path):
    stones = helpers.parse_to_int_lists(path)[0]    
    return calc(stones, 25), calc(stones, 75)

if __name__ == '__main__':
    print(run("test/day11.txt"))
    print(run("data/day11.txt"))
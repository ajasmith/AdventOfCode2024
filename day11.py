from math import floor, log
import helpers

seen = {}

def n_digits(x):
    if (x == 0):
        return 1
    else:
        return floor(log(x, 10)) + 1

def split_stone(stone):
    s = str(stone)
    mid = int(len(s)/2)
    return [int(s[0:mid]), int(s[mid:len(s)])]

def blink_stone(stone):
    if (stone == 0):
        return [1]
    elif (n_digits(stone) % 2 == 0):
        return split_stone(stone)
    else:
        return [stone * 2024]

def blink(stones):
    new_stones = []
    for s in stones:
        new_stones.extend(blink_stone(s))
    return new_stones

def run(path):
    stones = helpers.parse_to_int_lists(path)[0]

    count = [len(stones)]
    n = [25]

    for i in range(0, max(n)):
        stones = blink(stones)
        count.append(len(stones))
    
    return list(map(lambda i: count[i], n))

if __name__ == '__main__':
    print(run("test/day11.txt"))
    #print(run("data/day11.txt"))
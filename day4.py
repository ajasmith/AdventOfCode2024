import numpy
import helpers

def valid_pos(x, y, w, h):
    return x >= 0 and x < w and y >= 0 and y < h

def get_all_valid_dir(x, y, w, h, phrase_len):
    all_dir = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    dir = list()
    for d in all_dir:
        end_x = x + d[0] * (phrase_len - 1)
        end_y = y + d[1] * (phrase_len - 1)
        if valid_pos(end_x, end_y, w, h):
            dir.append(d)
    return dir

def get_next_char(arr, x, y, dir, idx):
    return arr[x + dir[0] * idx, y + dir[1] * idx]

def check_from_pos1(arr, x, y, w, h, phrase):
    count = 0
    if (arr[x,y] == phrase[0]):
        phrase_len = len(phrase)
        dirs = get_all_valid_dir(x, y, w, h, phrase_len)
        for dir in dirs:
            good_dir = True
            for idx in range(1,phrase_len):
                if get_next_char(arr, x, y, dir, idx) != phrase[idx]:
                    good_dir = False
                    break
            if good_dir:
                count += 1
    return count

def run1(arr):
    phrase = [b'X', b'M', b'A', b'S']
    w = numpy.size(arr, 0)
    h = numpy.size(arr, 1)
    count = 0

    for y in range(0, h):
        for x in range(0, w):
            count += check_from_pos1(arr, x, y, w, h, phrase)
    return count

def part1(path):
    arr = helpers.parse_to_char_array(path)
    print(run1(arr))

def valid_mas(c1, c2):
    fwd = c1 == b'M' and c2 == b'S'
    bwd = c1 == b'S' and c2 == b'M'
    return fwd or bwd

def check_from_pos2(arr, x, y):
    if arr[x,y] == b'A':
        c1 = arr[x-1,y-1]
        c2 = arr[x+1,y+1]
        if valid_mas(c1,c2):
            c3 = arr[x-1, y+1]
            c4 = arr[x+1, y-1]
            if (valid_mas(c3,c4)):
                return 1
    return 0

def run2(arr):
    w = numpy.size(arr, 0)
    h = numpy.size(arr, 1)
    count = 0
    for y in range(1, h-1):
        for x in range(1, w-1):
            count += check_from_pos2(arr, x,y)
    return count

def part2(path):
    arr = helpers.parse_to_char_array(path)
    print(run2(arr))

part1("test/day4.txt")
part1("data/day4.txt")
part2("test/day4.txt")
part2("data/day4.txt")
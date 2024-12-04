import helpers

all_directions = [ (0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1) ]

def valid_pos(x, y, w, h):
    return x >= 0 and x < w and y >= 0 and y < h

def get_char(arr, x, y, dir, idx):
    return arr[x + dir[0] * idx, y + dir[1] * idx]

def count_XMASs_at_pos(arr, x, y, w, h):
    count = 0
    if arr[x, y] == b'X':
        for drn in all_directions:
            if valid_pos(x + drn[0]*3, y + drn[1]*3, w, h):
                if get_char(arr, x, y, drn, 1) == b'M':
                    if get_char(arr, x, y, drn, 2) == b'A':
                        if get_char(arr, x, y, drn, 3) == b'S':
                            count += 1
    return count

def check_for_X_at_position(arr, x, y):
    if arr[x,y] == b'A':
        def valid(m, s):
            return m == b'M' and s == b'S'
        c1 = arr[x-1,y-1]
        c2 = arr[x+1,y+1]
        if valid(c1,c2) or valid(c2,c1):
            c3 = arr[x-1, y+1]
            c4 = arr[x+1, y-1]
            if (valid(c3,c4) or valid(c4,c3)):
                return 1
    return 0

def part1(path):
    arr, w, h = helpers.parse_to_char_array(path)
    count = 0
    for y in range(0,h):
        for x in range(0,w):
            count += count_XMASs_at_pos(arr,x,y,w,h)
    print(count)

def part2(path):
    arr, w, h = helpers.parse_to_char_array(path)
    count = 0
    for y in range(1, h-1):
        for x in range(1, w-1):
            count += check_for_X_at_position(arr, x,y)
    print(count)

part1("test/day4.txt")
part1("data/day4.txt")
part2("test/day4.txt")
part2("data/day4.txt")
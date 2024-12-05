import numpy

def open_file(path):
    with open(path, "r") as file:
        data = list(map(lambda s: s.replace('\n', ''), file.readlines()))
        return data

def parse_to_int_lists(path):
    lines = open_file(path)
    data = list(map(str.split, lines))
    ints = list(map(lambda x: list(map(int, x)), data))
    return ints

def parse_to_char_array(path):
    lines = open_file(path)
    h = len(lines)
    w = len(lines[0]) if h > 0 else 0

    arr = numpy.empty((w,h), dtype='|S1', order='F')
    y = 0
    for line in lines:
        for x in range(0,w):
            arr[x,y] = line[x]
        y += 1
    return arr, w, h
import numpy

def open_file(path):
    with open(path, "r") as file:
        data = file.readlines()
        return data

def parse_to_int_lists(path):
    lines = open_file(path)
    data = list(map(str.split, lines))
    ints = list(map(lambda x: list(map(int, x)), data))
    return ints

def parse_to_char_array(path):
    lines = open_file(path)
    w = len(lines[0]) - 1
    h = len(lines)

    arr = numpy.empty((w,h), numpy.character)
    y = 0
    for line in lines:
        for x in range(0,w):
            arr[x,y] = line[x]
        y += 1
    return arr, w, h
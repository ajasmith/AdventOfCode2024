def open_file(path):
    with open(path, "r") as file:
        data = file.readlines()
        return data

def parse_to_int_lists(path):
    lines = open_file(path)
    data = list(map(str.split, lines))
    ints = list(map(lambda x: list(map(int, x)), data))

    return ints
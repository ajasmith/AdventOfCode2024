import helpers

def parse(path):
    m, w, h = helpers.parse_to_char_array(path)
    antennas = {}
    for y in range(0,h):
        for x in range(0,w):
            key = m[x,y].decode('ascii')
            if (key != '.'):
                if (key not in antennas):
                    antennas[key] = list()
                antennas[key].append((x,y))
    return antennas, w, h

def in_bounds(p, w, h):
    return p[0] >= 0 and p[0] < w and p[1] >= 0 and p[1] < h

def diff(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

def plus(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def calculate_antinodes_for_antenna_pair(a, b, w, h, part1):
    d = diff(a, b)
    anodes = set()

    if (part1):
        anodes.add(diff(d,a))
        anodes.add(plus(d,b))
        anodes = set(filter(lambda p: in_bounds(p, w, h), anodes))
    else:
        x = b
        while in_bounds(x, w, h):
            anodes.add(x)
            x = plus(d, x)
        x = a
        while in_bounds(x, w, h):
            anodes.add(x)
            x = diff(d, x)

    return anodes

def find_all_valid_antinodes(nodes, w, h, part1):
    if (len(nodes) < 2):
        return set()

    antinodes = find_all_valid_antinodes(nodes[1:], w, h, part1)

    n0 = nodes[0]
    for n1 in nodes[1:]:
        antinodes |= calculate_antinodes_for_antenna_pair(n0, n1, w, h, part1)

    return antinodes

def count_antinodes(antennas, w, h, part1):
    all_antinodes = set()
    for node in antennas:
        all_antinodes |= find_all_valid_antinodes(antennas[node], w, h, part1)
    return len(all_antinodes)

def run(path):
    a, w, h  = parse(path)
    return (count_antinodes(a, w, h, True), count_antinodes(a, w, h, False))

if __name__ == '__main__':
    print(run("test/day8.txt"))
    print(run("data/day8.txt"))
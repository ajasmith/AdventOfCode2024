import helpers

turn_map = {b'^': b'>', b'>': b'v', b'v': b'<', b'<': b'^'}
fwd_map = {b'^': 1, b'>': 1000, b'v': -1, b'<': -1000}

def pos_to_int(x,y):
    return x * 1000 + y

def int_to_pos(i):
    return i // 1000, i % 1000

def parse_input(path):
    grid, w, h = helpers.parse_to_char_array(path)
    obstacles = set()
    guard = -1, b'X'
    for y in range(0,h):
        for x in range(0, w):
            c = grid[x,y]   
            if c == b'#':
                obstacles.add(pos_to_int(x,y))
            elif c != b'.':
                guard = pos_to_int(x, y), b'^'
    return guard, obstacles, w, h

def forward(guard):
    p, o = guard
    return p + fwd_map[o], o

def turn(guard):
    p, o = guard
    return p, turn_map[o]

def move_guard(guard, obstacles):
    fwd = forward(guard)
    if (fwd[0]) in obstacles:
        return turn(guard)
    else:
        return fwd

def in_bounds(guard, w, h):
    p, _ = guard
    x, y = int_to_pos(p)
    return x >= 0 and y >= 0 and x < w and y < h

def is_circular(g, obstacles, extra, w, h):
    visited = set()
    o = obstacles.union({extra})
    while in_bounds(g, w, h):
        if g in visited:
            return True
        else:
            visited.add(g)
            g = move_guard(g, o)
    return False

def run(path):
    g, o, w, h = parse_input(path)
    
    visited = set()
    circular_count = 0

    while in_bounds(g, w, h):
        visited.add(g[0])
        fwd = forward(g)
        if (fwd[0]) in o:
            g = turn(g)
        else:
            if fwd[0] not in visited and is_circular(turn(g), o, fwd[0], w, h):
                circular_count += 1
            g = fwd

    return len(visited), circular_count

if __name__ == '__main__':
    print(run("test/day6.txt"))
    print(run("data/day6.txt"))
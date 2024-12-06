from datetime import *
import helpers

turn_map = {b'^': b'>', b'>': b'v', b'v': b'<', b'<': b'^'}
fwd_map = {b'^': 1, b'>': 1000, b'v': -1, b'<': -1000}

# Failed attempt to make set lookup faster by moving from tuples to ints
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

def run_route(g, obstacles, w, h):
    route = list()
    circular = False
    while in_bounds(g, w, h) and not circular:
        if g in route:
            circular = True
        else:
            route.append(g)
            g = move_guard(g, obstacles)
    return route, circular

def run(path):
    g, o, w, h = parse_input(path)

    # part 1
    route, _ = run_route(g, o, w, h)
    visited = set(map(lambda g: g[0], route))

    # part 2
    loop_count = 0
    for new_obstacle in visited:
        if new_obstacle == g[0]:
            continue

        _, circular = run_route(g, o.union({new_obstacle}), w, h)
    
        if (circular):
            loop_count += 1

    return len(visited), loop_count

if __name__ == '__main__':
    for i in range(0,20):
        print(run("test/day6.txt"))
    #print(run("data/day6.txt"))
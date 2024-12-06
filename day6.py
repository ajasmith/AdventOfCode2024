import helpers

turn_map = {b'^': b'>', b'>': b'v', b'v': b'<', b'<': b'^'}
fwd_map = {b'^': (0,1), b'>': (1,0), b'v': (0,-1), b'<': (-1,0)}

def parse_input(path):
    grid, w, h = helpers.parse_to_char_array(path)
    obstacles = set()
    guard = -1, -1, b'X'
    for y in range(0,h):
        for x in range(0, w):
            c = grid[x,y]   
            if c == b'#':
                obstacles.add((x,y))
            elif c != b'.':
                guard = x, y, b'^'
    return guard, obstacles, w, h

def forward(guard):
    x, y, orientation = guard
    dx, dy = fwd_map[orientation]
    return x + dx, y + dy, orientation

def turn(guard):
    x, y, orientation = guard
    return x, y, turn_map[orientation]

def move_guard(guard, obstacles):
    fwd = forward(guard)
    if (fwd[0], fwd[1]) in obstacles:
        return turn(guard)
    else:
        return fwd

def in_bounds(guard, w, h):
    x, y, _ = guard
    return x >= 0 and y >= 0 and x < w and y < h

def draw(route, obstacle, w, h):
    def calc_range(idx, lim):
        v = list(map(lambda r: r[idx], route))
        return (max([min(v)-1,0]), min([max(v)+1, lim-1]))
    xr = calc_range(0, w)
    yr = calc_range(1, h)

    m = ["." * (xr[1]-xr[0] + 1)] * (yr[1] - yr[0] + 1)

    def put_char(x, y, c):
        if x >= xr[0] and x <= xr[1] and y >= yr[0] and y <= yr[1]:
            px = x - xr[0]
            py = yr[1] - y
            old = m[py]
            m[py] = old[:px] + c + old[px+1:]

    for r in route:
        put_char(r[0], r[1], r[2].decode('ascii'))

    for o in obstacle:
        put_char(o[0], o[1], "#")

    for s in m:
        print(s)

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
    g, obstacles, w, h = parse_input(path)
    start = g[0], g[1]

    # part 1
    route, _ = run_route(g, obstacles, w, h)
    visited = set(map(lambda g: (g[0], g[1]), route))

    # part 2
    loop_obstacle = set()
    for r in route:
        f = forward(r)
        fx, fy = f[0], f[1]
        if (fx,fy) not in obstacles and (fx,fy) != start:
            o = obstacles.union({(fx, fy)})
            rr, circular = run_route(turn(r), o, w, h)
            if (circular):
                loop_obstacle.add((fx, fy))

    return len(visited), len(loop_obstacle)

if __name__ == '__main__':
    print(run("test/day6.txt"))
    print(run("data/day6.txt"))
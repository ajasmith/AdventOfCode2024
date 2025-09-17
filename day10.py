import helpers

def pos_to_int(x,y):
    return x * 1000 + y

def parse_input(path):
    grid, w, h = helpers.parse_to_char_array(path)
    terrain = {}
    for y in range(0,h):
        for x in range(0, w):
            terrain[pos_to_int(x,y)] = int(grid[x,y])
    return terrain

def move(pos, dir):
    fwd_map = {b'^': 1, b'>': 1000, b'v': -1, b'<': -1000}
    return pos + fwd_map[dir]

def valid(terrain, curr, next):
    return next in terrain and terrain[next] == terrain[curr] + 1

def walk_to_peaks(t, start):
    queue = [start]
    visited = {}
    while (len(queue) > 0):
        curr = queue.pop()

        if (t[curr] == 9):
            if (curr not in visited):
                visited[curr] = 1
            else:
                visited[curr] += 1
            continue

        for dir in [b'^', b'>', b'v', b'<']:
            next = move(curr, dir)
            if (valid(t, curr, next)):
                queue.append(next)
    return visited

def run(path):
    t = parse_input(path)
    part1 = 0
    part2 = 0

    for start in t:
        if (t[start] == 0):
            visited = walk_to_peaks(t, start)
            part1 += len(visited)
            part2 += sum(visited.values())
    
    return part1, part2

if __name__ == '__main__':
    print(run("test/day10.txt"))
    print(run("data/day10.txt"))
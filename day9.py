import helpers

def part1(path):
    line = (helpers.open_file(path))[0]
    x = [int(ch) for ch in line]

    # Move from the front and the back simultaneously
    curr = 0
    left = 0
    right = len(x)-1
    rightcount = x[right]

    checksum = 0

    while left < right:
        # Advance past the current file moving forwards.
        for _ in range(0, x[left]):
            currFileIndex = int(left/2)
            checksum += curr * currFileIndex
            curr += 1

        left += 1

        for _ in range(0, x[left]):
            if (rightcount == 0):
                right -= 2
                rightcount = x[right]

            currFileIndex = int(right/2)
            checksum += curr * currFileIndex
            curr += 1
            rightcount -= 1

        left += 1

    for _ in range (0, rightcount):
        currFileIndex = int(right/2)
        checksum += curr * currFileIndex
        curr += 1 

    return checksum

class File: 
    id: int
    size: int
    pos: int

    def __init__(self, id, size, pos):
        self.id = id
        self.size = size
        self.pos = pos

def calculate_checksum(files):
    checksum = 0
    for file in files.values():
        for i in range(0, file.size):
            checksum += file.id * (file.pos + i)
    return checksum

def first_space(spaces, required, max_pos):
    idx = 0
    for (pos, size) in spaces:
        if (pos >= max_pos):
            return -1
        elif (size >= required):
            return idx
        idx += 1
    return -1

def parse(path):
    line = (helpers.open_file(path))[0]
    x = [int(ch) for ch in line]
    files = {}
    spacemap = []
    file = 0
    pos = 0
    for i in range(0, len(x)):
        filesize = x[i]
        isFile = (i % 2) == 0
        if (isFile):
            files[file] = File(file, filesize, pos)
            file += 1
        else:
            spacemap.append((pos, filesize))
        pos += filesize
    
    return files, spacemap

def part2(path):
    files, spaces = parse(path)

    for file in range(len(files)-1,0, -1):
        required_space = files[file].size
        idx = first_space(spaces, required_space, files[file].pos)
        if (idx != -1):
            pos, size = spaces[idx]
            files[file].pos = pos
            if (size == files[file].size):
                spaces.pop(idx)
            else:
                spaces[idx] = (pos + files[file].size, size - files[file].size)
    return calculate_checksum(files)

def run(path):
    return (part1(path), part2(path))


if __name__ == '__main__':
    print(run("test/day9.txt"))
    print(run("data/day9.txt"))
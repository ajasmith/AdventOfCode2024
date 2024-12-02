import helpers

def next_is_safe(prev, curr, next):
    is_same_drn = (prev < 0) or ((next-curr) * (curr-prev) > 0)
    if (not is_same_drn): return False

    is_safe_jump = (curr < 0) or (abs(next-curr) < 4)
    if (not is_safe_jump): return False

    return True

def get_index_with_skip(index, skip_index):
    if (skip_index == -1 or index < skip_index):
        return index
    return index + 1

def safe_report(report, skip_index):
    length = len(report)
    if (skip_index >= 0):
        length -= 1

    prev = -1
    curr = report[get_index_with_skip(0, skip_index)]

    for i in range(1, length):
        next = report[get_index_with_skip(i, skip_index)]

        if (not(next_is_safe(prev, curr, next))):
            return False
        
        prev = curr
        curr = next

    return True

def safe_report_part1(report):
    return safe_report(report, -1)

def run_part1(path):
    reports = helpers.parse_to_int_lists(path)
    safe = list(filter(safe_report_part1, reports))
    print(len(safe))

run_part1("test_data/day2.txt")
run_part1("data/day2.txt")


def safe_report_part2(report):
    if (safe_report(report, -1)):
        return True
    
    for i in range(0, len(report)):
        if (safe_report(report, i)):
            return True
    
    return False

def run_part2(path):
    reports = helpers.parse_to_int_lists(path)
    safe = list(filter(safe_report_part2, reports))
    print(len(safe))

run_part2("test_data/day2.txt")
run_part2("data/day2.txt")
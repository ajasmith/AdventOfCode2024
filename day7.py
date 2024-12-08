import helpers

def parse(path):
    lines = helpers.open_file(path)
    data = list(map(lambda s: str.split(s.replace(":", "")), lines))
    return list(map(lambda x: list(map(int, x)), data))

def apply_operator(a, operator, b):
    if operator == '+':
        return a + b
    elif operator == '*':
        return a * b
    elif operator == '||':
        return int(str(a) + str(b))
    else:
        raise NotImplementedError

def check(expected, current, next_symbol, remaining_vars, part2):
    if len(remaining_vars) == 0:
        return current == expected
    elif (current > expected):
        return False
    else:
        next = apply_operator(current, next_symbol, remaining_vars[0])

        return check(expected, next, '+', remaining_vars[1:], part2) \
            or check(expected, next, '*', remaining_vars[1:], part2) \
            or (part2 and check(expected, next, '||', remaining_vars[1:], part2))

def check_all_possible(equation, part2):
    return check(equation[0], 0, '+', equation[1:], part2)

def run(path):
    equations = parse(path)

    answer = {False: 0, True: 0}
    for part2 in [False, True]:
        for e in equations:
            if check_all_possible(e, part2):
                answer[part2] += e[0]

    return (answer[False], answer[True])

if __name__ == '__main__':
    print(run("test/day7.txt"))
    print(run("data/day7.txt"))
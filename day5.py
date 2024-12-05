import helpers

def add_rule(rules, rule):
    if rule[0] in rules:
        rules[rule[0]].add(rule[1])
    else:
        rules[rule[0]] = { rule[1] }

def parse_input(path):
    data = helpers.open_file(path)
    rules = {}
    updates = list()
    section = 1
    for line in data:
        if len(line) == 0:
            section = 2
        elif section == 1:
            pair = map(int, line.split('|'))
            add_rule(rules, (next(pair), next(pair)))
        else:
            updates.append(list(map(int, line.split(','))))
    return rules, updates

def check_and_fix(rules, update):
    ok = True
    valid_update = update[0:1]
    for page in update[1:]:
        insert_at = len(valid_update)
        while page in rules and len(rules[page].intersection(valid_update[0:insert_at])) > 0:
            ok = False
            insert_at -= 1
        valid_update.insert(insert_at, page)
    return ok, valid_update

def run(path):
    rules, updates = parse_input(path)
    scores = [0, 0]
    for u in updates:
        ok, u = check_and_fix(rules, u)
        scores[0 if ok else 1] += u[len(u) // 2]
    return scores

if __name__ == '__main__':
    print(run("test/day5.txt"))
    print(run("data/day5.txt"))
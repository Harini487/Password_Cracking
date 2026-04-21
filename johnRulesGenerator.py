commands = ["l", "sa@", "sE3", "so0", "si1", "ss$", "sS$", "st7", "sT7", "sA4", "Az\"[0-9][0-9][0-9][0-9]\""]

rules = [""]

for command in commands:
    new_rules = []
    for rule in rules:
        new_rule = f"{rule} {command}"
        new_rules.append(new_rule)
    rules += new_rules

rules.sort(key=len)

for rule in rules:
    print(rule)
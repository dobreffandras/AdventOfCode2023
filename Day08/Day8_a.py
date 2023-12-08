import re
from itertools import cycle

puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    def parse_row(row):
        m = re.match("([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", row)
        g1, g2, g3 = m.groups()
        return (g1, (g2, g3))
    
    instructions, maps_description = input.split("\n\n")
    return (cycle(instructions), dict(map(parse_row, maps_description.splitlines())))

def steps_count_finding_ZZZ(x):
    def to_idx(instruction):
        return 0 if instruction == 'L' else 1

    instructions, mapping = x
    steps_count = 0
    current_node = "AAA"
    while current_node != "ZZZ":
        instruction = next(instructions)
        current_node = mapping[current_node][to_idx(instruction)]
        steps_count+=1
    return steps_count
print(steps_count_finding_ZZZ(parse(puzzle_input)))
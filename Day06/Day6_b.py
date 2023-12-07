import re

puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    time_line, distance_line = input.splitlines()
    time = int(''.join(filter(lambda c: c.isdigit(), time_line)))
    distance = int(''.join(filter(lambda c: c.isdigit(), distance_line)))
    return time, distance

def calculate_winning_possibilities_count(race):
    race_time = race[0]
    record_distance = race[1]
    for i in range(1, race_time):
        j = (race_time - i)
        if record_distance <  i * j:
            return j - i + 1

print(calculate_winning_possibilities_count(parse(puzzle_input)))
import re
import math

puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    times_line, distances_line = input.splitlines()
    times = map(int, re.findall("(\d+)", times_line))
    distances = map(int, re.findall("(\d+)", distances_line))
    return zip(times, distances)

def play_races(races):
    def calculate_winning_possibilities_count(race):
        race_time = race[0]
        record_distance = race[1]
        for i in range(1, race_time):
            j = (race_time - i)
            if record_distance <  i * j:
                return j - i + 1
    
    return map(calculate_winning_possibilities_count, races)

print(math.prod(play_races(parse(puzzle_input))))
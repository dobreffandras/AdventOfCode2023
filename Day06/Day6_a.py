"""
Explanation:
Instead of calculating all possible outcomes of races
we find only the very first occurrence where the record is beat.
From then on we can calculate the all the winning possibilities.


i - velocity (millisecs of button push)
j - remaining time 
time = i + j
distance = i * j

So the best distance would be always (time/2)^2 i.e.  i = j 
Pairs closer to this will be higher.
So there is an interval of winning pairs where(i, j) beating record is the lower bound and (j, i) is the higher bound.
The size of this interval therefore i - j + 1

e.g:
time: 7
record: 9

0-7 => 0
1-6 => 6
2-5 => 10*
3-4 => 12*
4-3 => 12*
5-2 => 10*
6-1 => 6
7-0 => 0

count: 5-2+1 = 4
"""

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
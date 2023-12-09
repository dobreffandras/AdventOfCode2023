"""
Explanation:
The brute force solution does not work for this problem. It takes too long to execute.

The input problem is constructed in a way that from each starting node steps lead to an individual end node, and
from the end node steps lead to the same end node, not returning to the start node. 
Thus the path from the end node is a cycle.

Running this program will execute the steps from each start node leading to the end node, and then reaching the end node the second time.
The program prints out the number of steps on those paths.
From the result we can detect two things:
- The path from the starting node to the end node, and the path of the cycle back to the end node are equally long.
- The paths are way more longer than the step instructions. Moreover they are always the multiple of the instructions length.
  This means that on every path the instructions are executed as a whole (multiple times) until they reach the end node.
  
To find the step count where all of the executions reach the end note at the same time we need to repeat all cycles.
For ecxample
  A--Z--Z--Z--Z
  A---Z---Z---Z
  A-----Z-----Z
As the step count from start node to the end is equal to the step count of taking a cycle back to the end node, 
the problem can be simplifed to the following:
  Z--Z--Z--Z--Z  cycle-length: 3
  Z---Z---Z---Z  cycle-length: 4
  Z-----Z-----Z  cycle-length: 6
 
To find the steps count of reaching the end nodes simultaneously we need to find the least common multiple of the paths.
(In the above example: 12)
"""

import re
import os
import math
from functools import reduce
from itertools import cycle

puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    def parse_row(row):
        m = re.match("([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)", row)
        g1, g2, g3 = m.groups()
        return (g1, (g2, g3))
    
    instructions, maps_description = input.split("\n\n")
    return (instructions, dict(map(parse_row, maps_description.splitlines())))

def find_all_starting_nodes(nodes):
    return list(filter(lambda n: n[2] == 'A', nodes))
    
def all_nodes_finished(nodes):
    return all([n[2] == 'Z' for n in nodes])

def steps_count_finding_end_nodes(x):
    def to_idx(instruction):
        return 0 if instruction == 'L' else 1

    def run(starting_node, instruction_list):
        print(" Starting at node", starting_node)
        instructions = cycle(instruction_list)
        steps_count = 0
        end_node_already_reached = False
        current_node = starting_node
        path_length = 0
        while True:
            if current_node[2] == "Z":
                print("  --> Reached end node", current_node, "in steps", steps_count)
                if end_node_already_reached:
                    break
                end_node_already_reached = True
                path_length = steps_count
                steps_count = 0
            instruction = next(instructions)
            current_node = mapping[current_node][to_idx(instruction)]
            steps_count+=1
        print(" Finishing at node", current_node, os.linesep)
        return path_length
        
    instruction_list, mapping = x
    starting_nodes = find_all_starting_nodes(mapping.keys())
    
    return [run(starting_node, instruction_list) for starting_node in starting_nodes]

def lcm(numbers):
    return reduce(lambda a,b: abs(a*b) // math.gcd(a,b), numbers)
    
path_lengths = steps_count_finding_end_nodes(parse(puzzle_input))
print("Path lengths:", path_lengths)
print("LCM of path lengths:", lcm(path_lengths))
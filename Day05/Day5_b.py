"""
This is a brute force solution for Day5 B. Unfortunately the input contains so many seeds that the execution takes a very long time.
"""

from functools import reduce
from collections import namedtuple

puzzle_input = open("./puzzle_input.txt", "r").read()

MapRange = namedtuple("MapRange", ["low", "high", "offset"])

class Mapper:
    def __init__(self, mapping_definitions):
        self.map_ranges = list(map(self.convert_to_mapRange, mapping_definitions))
    
    def convert_to_mapRange(self, mapping):
        destination = mapping[0]
        source = mapping[1]
        length = mapping[2]
        
        low = source
        offset = destination - source
        high = source + length -1
        return MapRange(low, high, offset)
        
    def map(self, num):
        for r in self.map_ranges:
            if r.low <= num <= r.high:
                return num + r.offset
        return num

class Workflow:
    def __init__(self, seeds_range, mappers):
        self.seeds = seeds_range
        self.mappers = mappers
    
    def run(self):
        def execute_workflow_for_seed(seed):
            return reduce(lambda num, m: m.map(num), self.mappers, seed)
            
        return [execute_workflow_for_seed(seed) for seed in self.seeds]
        
def parse(input):
    def parse_header(header):
        return [int(s) for s in header.split(" ")[1:]]
    
    def parse_maps(maps):    
        map_definition_groups = [map_group.splitlines()[1:] for map_group in maps]
        return [[tuple(map(int, map_def.split(" "))) for map_def in map_def_group] for map_def_group in map_definition_groups]

    header, *maps = input.split("\n\n")
    return parse_header(header), parse_maps(maps)


def calculate_seed_ranges(seeds_input):
    seed_range_pairs = list(zip(seeds_input[::2], seeds_input[1::2]))
    return [range(i[0], i[0]+i[1]) for i in seed_range_pairs]

def execute_workflows(seed_ranges, mappers):
    locations = []
    for seed_range in seed_ranges:    
        print(seed_range, "count:", len(seed_range))
        workflow = Workflow(seed_range, mappers)
        workflow_locations = workflow.run()
        print("Workflow has ", len(workflow_locations), " locations")
        locations.append(min(workflow_locations))
    return locations

header, mapper_definitions = parse(puzzle_input)
mappers = [Mapper(m) for m in mapper_definitions]
print(len(mappers))
print(min(execute_workflows(calculate_seed_ranges(header), mappers)))
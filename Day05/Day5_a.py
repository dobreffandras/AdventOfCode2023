from functools import reduce
from collections import namedtuple

puzzle_input = open("./puzzle_input.txt", "r").read()

MapRange = namedtuple("MapRange", ["destination", "source", "length"])
        
class Mapper:

    def __init__(self, mapping_definitions):
        self.map_ranges = [MapRange(m[0], m[1], m[2]) for m in mapping_definitions]
        
    def map(self, num):
        for r in self.map_ranges:
            offset = r.destination - r.source
            if r.source <= num <= r.source + r.length -1:
                return num + offset
        return num

class Workflow:
    def __init__(self, workflow_descriptor):
        self.seeds =  workflow_descriptor[0]
        self.mappings = [Mapper(m) for m in workflow_descriptor[1]]
    
    def run(self):
        def execute_workflow_for_seed(seed):
            return reduce(lambda num, mapper: mapper.map(num), self.mappings, seed)
        
        return [execute_workflow_for_seed(seed) for seed in self.seeds]

def parse(input):
    def parse_header(header):
        return [int(s) for s in header.split(" ")[1:]]
    def parse_maps(maps):
        
        map_definition_groups = [map_group.splitlines()[1:] for map_group in maps]
        return [[tuple(map(int, map_def.split(" "))) for map_def in map_def_group] for map_def_group in map_definition_groups]

    header, *maps = input.split("\n\n")
    return parse_header(header), parse_maps(maps)

workflow = Workflow(parse(puzzle_input))
locations = workflow.run()
print(min(locations))
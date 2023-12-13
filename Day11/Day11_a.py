import itertools

puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    return [[c for c in line] for line in input.splitlines()]
    
def expand_universe(universe):
    def find_indexes_of_empty_rows():
        return [i for i in range(len(universe)) if all([c == '.' for c in universe[i]])]
    def find_indexes_of_empty_columns():
        return [j for j in range(len(universe[0])) if all([row[j] == '.' for row in universe])]
        
    empty_row_indices = find_indexes_of_empty_rows()
    empty_colum_indices = find_indexes_of_empty_columns()

    expanded_universe = []
    for i in range(len(universe)):
        row = []
        for j in range(len(universe[0])):
            row.append(universe[i][j])
            if j in empty_colum_indices:
                row.append('.')
        expanded_universe.append(row)
        if i in empty_row_indices:
            expanded_universe.append(['.'] * len(row))
    return expanded_universe
        
def collect_galaxy_coordinates(universe):
    return [(i,j) for i in range(len(universe)) for j in range(len(universe[0])) if universe[i][j] == '#']

def create_coordinate_pairs(coordinates):
    return list(itertools.combinations(coordinates, 2))

def calculate_distances(coordinate_pairs):
    def calculate_distance(pair):
        (ax, ay), (bx, by) = pair
        return abs(ax-bx) + abs(ay-by)
        
    return map(calculate_distance, coordinate_pairs)

expanded_universe = expand_universe(parse(puzzle_input))
#print('\n'.join([''.join(line) for line in expanded_universe]))
print(sum(calculate_distances(create_coordinate_pairs(collect_galaxy_coordinates(expanded_universe)))))

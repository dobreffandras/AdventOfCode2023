import itertools

puzzle_input = open("./puzzle_input.txt", "r").read()
        

def parse(input):
    return [[c for c in line] for line in input.splitlines()]

def collect_galaxy_coordinates(universe, factor):
    def find_indexes_of_empty_rows():
        return [i for i in range(len(universe)) if all([c == '.' for c in universe[i]])]
    def find_indexes_of_empty_columns():
        return [j for j in range(len(universe[0])) if all([row[j] == '.' for row in universe])]
        
    empty_row_indices = find_indexes_of_empty_rows()
    empty_colum_indices = find_indexes_of_empty_columns()
    
    galaxy_coordinates = []
    i_exp = 0
    j_exp = 0
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            if universe[i][j] == '#':
                galaxy_coordinates.append((i_exp, j_exp))
            if j in empty_colum_indices:
                j_exp += factor
            else:
                j_exp += 1
        
        j_exp = 0
        if i in empty_row_indices:
            i_exp += factor
        else:
            i_exp += 1

    return galaxy_coordinates

def create_coordinate_pairs(coordinates):
    return list(itertools.combinations(coordinates, 2))

def calculate_distances(coordinate_pairs):
    def calculate_distance(pair):
        (ax, ay), (bx, by) = pair
        return abs(ax-bx) + abs(ay-by)
        
    return map(calculate_distance, coordinate_pairs)


if __name__ == "__main__":
    print(sum(calculate_distances(create_coordinate_pairs(collect_galaxy_coordinates(parse(puzzle_input), 1_000_000)))))

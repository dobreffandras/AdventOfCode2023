puzzle_input = open("./puzzle_input.txt", "r").read()
schematic  = puzzle_input.splitlines()
H = len(schematic)
W = len(schematic[0])

def get_numbers_and_coordinates():
    coordinate_number_lookup = dict()
    coordinate_groups = []
    for i in range(0, H):
        number = ""
        coords = []
        for j in range(0, W):
            char = schematic[i][j]
            if char.isdigit():
                number += char
                coords.append((i,j))
            else:
                if(0 < len(number)):
                    coordinate_groups.append(coords)
                    for coord in coords:
                        coordinate_number_lookup[coord] = int(number)
                number = ""
                coords = []
                
        if(0 < len(number)):
            coordinate_groups.append(coords)
            for coord in coords:
                coordinate_number_lookup[coord] = int(number)
    return coordinate_number_lookup, coordinate_groups      

def process_neighbouring_numbers(i, j, coordinate_number_lookup, coordinate_groups):

    def generate_neighbouring_coordinates(i, j):
        coordinates = []
        if 0 < i and 0 < j:
            coordinates.append((i-1, j-1)) 
        if 0 < i and 0 < j:
            coordinates.append((i-1, j))
        if 0 < i and j < W-1:
            coordinates.append((i-1, j+1))    
        if 0 < j:
            coordinates.append((i, j-1)) 
        if j < W-1:
            coordinates.append((i, j+1))
        if i < H-1 and 0 < j:
            coordinates.append((i+1, j-1)) 
        if i < H-1 and 0 < j:
            coordinates.append((i+1, j))
        if i < H-1 and j < W-1:
            coordinates.append((i+1, j+1))
        return coordinates

    neighbouring_numbers = []
    coordinates_of_already_checked_number = []
    for coord in generate_neighbouring_coordinates(i, j):
       if coord in coordinate_number_lookup and coord not in coordinates_of_already_checked_number:
           neighbouring_numbers.append(coordinate_number_lookup[coord])
           
           group = next(g for g in coordinate_groups if coord in g)
           coordinates_of_already_checked_number.extend(group)
           
    return neighbouring_numbers

coordinate_number_lookup, coordinate_groups = get_numbers_and_coordinates()
reachable_numbers = []
for i in range(0, H):
    for j in range(0, W):
        char = schematic[i][j]
        if not char.isdigit() and char != '.':
            neighbouring_numbers = process_neighbouring_numbers(i, j, coordinate_number_lookup, coordinate_groups)
            reachable_numbers.extend(neighbouring_numbers)
            
print(sum(reachable_numbers))
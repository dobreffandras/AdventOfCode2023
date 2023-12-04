puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    def parse_line(line):
        card_body = line.split(":")[1]
        winning_part, own_numbers_part = card_body.split("|")
        winning_numbers = [int(n) for n in winning_part.split(" ") if n]
        own_numbers = [int(n) for n in own_numbers_part.split(" ") if n]
        
        return winning_numbers, own_numbers
        
    return [parse_line(line) for line in input.splitlines()]
    
def calculate_card_duplication_occurrences(cards):
    def create_computation_table():
        table = dict()
        for i in range(0, len(cards)):
            table[i+1] = [cards[i], 1]
        return table
    
    computation_table = create_computation_table()
    
    for card_id in computation_table:
        card = computation_table[card_id][0]
        occurence = computation_table[card_id][1]
        winning_numbers, own_numbers = card
        winners = [n for n in own_numbers if n in winning_numbers]
        for offset in range(1, len(winners) + 1):
            computation_table[card_id + offset][1] += occurence
            
    return [c[1] for c in computation_table.values()]

print(sum(calculate_card_duplication_occurrences(parse(puzzle_input))))
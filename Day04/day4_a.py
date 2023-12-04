puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    def parse_line(line):
        card_body = line.split(":")[1]
        winning_part, own_numbers_part = card_body.split("|")
        winning_numbers = [int(n) for n in winning_part.split(" ") if n]
        own_numbers = [int(n) for n in own_numbers_part.split(" ") if n]
        
        return winning_numbers, own_numbers
        
    return [parse_line(line) for line in input.splitlines()]
    
def calculate_point(card):
    winning_numbers, own_numbers = card
    winners = [n for n in own_numbers if n in winning_numbers]
    return 2 ** (len(winners) - 1) if len(winners) else 0

print(sum([calculate_point(card) for card in parse(puzzle_input)]))
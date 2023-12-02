import re

puzzle_input = open("./puzzle_input.txt", "r").read()

class Round:
    def __init__(self, green, red, blue):
        self.green = green
        self.red = red
        self.blue = blue

    def __repr__(self):
        return "Round(g: {}, r: {}, b: {})".format(self.green, self.red, self.blue)
    

class Game:
    def __init__(self, identifier, rounds):
        self.id = identifier
        self.rounds = rounds
        
    def minimal_cubes(self):
        transposed_rounds = tuple(zip(*[[r.green, r.red, r.blue] for r in self.rounds]))
        return {
            'green': max(transposed_rounds[0]),
            'red': max(transposed_rounds[1]),
            'blue': max(transposed_rounds[2])
        } 
    
    def __repr__(self):
        return "Game({}, {})".format(self.id, self.rounds)
        

def parse(input):
    def parse_round(round_string):
        def get_value(regex_pattern):
            if regex_pattern.match(round_string):
                return int(regex_pattern.search(round_string).group(1))
            else:
                return 0

        green = get_value(re.compile(".* (\d+) green.*"))
        red = get_value(re.compile(".* (\d+) red.*"))
        blue = get_value(re.compile(".* (\d+) blue.*"))
        
        return Round(green, red, blue)
        
    def parse_game(game_string):
        game_head, game_body = game_string.split(":")
        identifier = int(re.search(r"\d+", game_head)[0])
        rounds = list(map(parse_round, game_body.split(";")))
        return Game(identifier, rounds)

    return list(map(parse_game, input.splitlines()))
    
def product_of_cubes(cubes):
    return cubes['green'] * cubes['red'] * cubes['blue']

print(sum([product_of_cubes(g.minimal_cubes()) for g in parse(puzzle_input)]))
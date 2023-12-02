import re

puzzle_input = open("./puzzle_input.txt", "r").read()

class Round:
    def __init__(self, green, red, blue):
        self.green = green
        self.red = red
        self.blue = blue
    
    def is_possible_for(self, max_green, max_red, max_blue):
        return self.green <= max_green and self.red <= max_red and self.blue <= max_blue
    
    def __repr__(self):
        return "Round(g: {}, r: {}, b: {})".format(self.green, self.red, self.blue)
    

class Game:
    def __init__(self, identifier, rounds):
        self.id = identifier
        self.rounds = rounds
        
    def is_possible_for(self, max_green, max_red, max_blue):
        return all([r.is_possible_for(max_green, max_red, max_blue) for r in self.rounds])
    
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
    
print(sum([g.id for g in filter(lambda x: x.is_possible_for(13, 12, 14), parse(puzzle_input))]))
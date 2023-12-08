from functools import cmp_to_key
from collections import Counter

puzzle_input = open("./puzzle_input.txt", "r").read()
cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

class Player:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.score = (self.hand_type(hand), self.score_by_card(hand))
        
    def hand_type(self, hand):
        if hand == "JJJJJ":
            return 6 # five of a kind

        c = Counter(hand)
        countJ = c['J']
        del c['J']
        most_common_card = c.most_common(1)[0][0]
        c.update({ most_common_card: countJ})
        m = [mc[1] for mc in c.most_common(2)]
        
        match m:           
            case [5]:
                return 6 # five of a kind
            case [4,1]:
                return 5 # four of a kind
            case [3,2]:
                return 4 # full house
            case [3,1]:
                return 3 # three of a kind
            case [2,2]:
                return 2 # two pairs
            case [2,1]:
                return 1 # one pair
            case _:
                return 0 # high card
        
    def score_by_card(self, hand):
        score = 0
        for i in range(0, len(hand)):
            idx = cards.index(hand[i])
            score += (100 ** (5 - i - 1)) * (idx+1)
        return score
        
    def __repr__(self):
        return "Player(hand={}, bid={}, score={}".format(self.hand, self.bid, self.score)

def parse(input):
    def parse_row(row):
        hand, bid = row.split(" ")
        return Player(hand, int(bid))
    
    return map(parse_row, input.splitlines())

def sort_players(players):    
    return sorted(players, key=lambda p: p.score)

def calculate_winnings(sorted_players):
    for i in range(0, len(sorted_players)):
        rank = i + 1
        yield sorted_players[i].bid * rank

if __name__ == "__main__":
    print(sum(calculate_winnings(sort_players(parse(puzzle_input)))))
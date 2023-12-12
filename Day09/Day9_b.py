import re
import os

puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    def parse_row(row):
        return list(map(int, re.findall("(-?\d+)", row)))
    
    return list(map(parse_row, input.splitlines()))

def find_predicted_begin_value(sequence):
    def calculate_sub_sequence(seq):
        a = seq[0]
        subsequence = [] 
        for i in range(1, len(seq)):
            b = seq[i]
            subsequence.append(b-a)
            a = b
        return subsequence
    
    def find_predicted_begin_value_recursive(seq):
        if all([x == 0 for x in seq]):
            return 0
        subsequence = calculate_sub_sequence(seq)
        sub_begin = find_predicted_begin_value_recursive(subsequence)
        seq_begin = seq[0]
        return seq_begin - sub_begin

    return find_predicted_begin_value_recursive(sequence)
    
print(sum(map(find_predicted_begin_value, (parse(puzzle_input)))))
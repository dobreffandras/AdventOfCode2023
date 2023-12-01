import re

puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    return input.splitlines()
    
def clean_calibration_values(dirty_calibration_values):
    return [clean_calibration_value(calib_val) for calib_val in dirty_calibration_values]
    
def clean_calibration_value(dirty_calibration_value):
    def find_all_indices_of(word, char_sequence):
        return [match.start() for match in re.finditer(word, char_sequence)]

    def get_values_with_indices(char_sequence):
        words = {
            '1': 1 , 
            '2': 2, 
            '3': 3, 
            '4': 4, 
            '5': 5, 
            '6': 6, 
            '7': 7, 
            '8': 8, 
            '9': 9,
            'one': 1 , 
            'two': 2, 
            'three': 3, 
            'four': 4, 
            'five': 5, 
            'six': 6, 
            'seven': 7, 
            'eight': 8, 
            'nine': 9
        }
   
        word_values_with_indices = []
        
        for word in words:
            for found_index in find_all_indices_of(word, char_sequence):
                word_values_with_indices.append((words[word], found_index))
        
        return list(filter(lambda x: x[1] != -1 , word_values_with_indices))
    
    found_values_with_indeces = get_values_with_indices(dirty_calibration_value)
    first_value = min(found_values_with_indeces, key=lambda x: x[1])[0]
    last_value = max(found_values_with_indeces, key=lambda x: x[1])[0]
    return first_value * 10 + last_value
 
print(sum(clean_calibration_values(parse(puzzle_input))))
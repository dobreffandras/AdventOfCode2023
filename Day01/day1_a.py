puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    return input.splitlines()
    
def clean_calibration_values(dirty_calibration_values):
    return [clean_calibration_value(calib_val) for calib_val in dirty_calibration_values]
    
def clean_calibration_value(dirty_calibration_value):
    def get_digit(char_sequence):
        return int(next(filter(lambda x: x.isdigit(), char_sequence)))

    first_digit = get_digit(dirty_calibration_value)
    last_digit = get_digit(reversed(dirty_calibration_value))
    return first_digit * 10 + last_digit
    
print(sum(clean_calibration_values(parse(puzzle_input))))
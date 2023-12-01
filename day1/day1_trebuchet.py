import re
from typing import List

def read_input() -> List[str]:
    with open('day1/input.txt') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    return lines

def part1_retrieve_calibrations(lines: List[str]) -> int:
    filtered_line = [list(filter(lambda line: line.isnumeric(), line)) for line in lines]
    
    calibrations = [int(nums[0] * 2) if len(nums) == 1 else int(nums[0] + nums[-1]) for nums in filtered_line]
    return sum(calibrations)

def valid_digit(string: str, early_flag: int) -> int:
    # early flag used to determine if we are looking for first or last digit
    digits_set = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}
    digit_map = {
        'one': 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    found_digit = -1
    found_idx = len(string) if early_flag else -1

    for digit in digits_set:
        if digit in string:
            # look for first occurence of the digit 
            if early_flag:
                curr_idx = string.find(digit)
                if found_idx > curr_idx:
                    found_idx, found_digit = curr_idx, digit
            # look for last occurence of the digit
            else:
                curr_idx = string.rfind(digit)
                if found_idx < curr_idx:
                    found_idx, found_digit = curr_idx, digit                

    return digit_map[found_digit] if found_digit != -1 else -1


def part2_retrieve_calibrations(lines: List[str]):
    digits = '1|2|3|4|5|6|7|8|9'

    # use regex to split line with digits
    chars = [re.split(digits, line) for line in lines]
    nums = [list(filter(lambda line: line.isnumeric(), line)) for line in lines]

    result = 0
    for i, component in enumerate(chars):
        first_digit, last_digit = int(nums[i][0]), int(nums[i][-1])

        # check if first digit is in chars
        search_digit = valid_digit(component[0], 1)
        first_digit = search_digit if search_digit != -1 else first_digit

        # check if last digit is in chars
        search_digit = valid_digit(component[-1], 0)
        last_digit = search_digit if search_digit != -1 else last_digit
        
        result += first_digit * 10 + last_digit
    
    return result

if __name__ == '__main__':
    lines = read_input()
    part1_retrieve_calibrations(lines)
    part2_retrieve_calibrations(lines)
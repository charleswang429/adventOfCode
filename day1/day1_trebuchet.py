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

def valid_digit(string: str) -> int:
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
    for digit in digits_set:
        if digit in string:
            return digit_map[digit]
    return -1

def part2_retrieve_calibrations(lines: List[str]):
    digits = '1|2|3|4|5|6|7|8|9'

    chars = [re.split(digits, line) for line in lines]
    nums = [list(filter(lambda line: line.isnumeric(), line)) for line in lines]

    result = 0
    for i, component in enumerate(chars):
        first_digit, last_digit = int(nums[i][0]), int(nums[i][-1])

        # check if first digit is in chars
        search_digit = valid_digit(component[0])
        first_digit = search_digit if search_digit != -1 else first_digit

        # check if last digit is in chars
        search_digit = valid_digit(component[-1])
        last_digit = search_digit if search_digit != -1 else last_digit
        
        result += first_digit * 10 + last_digit
    
    print(result)
    return result

if __name__ == '__main__':
    lines = read_input()
    # part1_retrieve_calibrations(lines)
    part2_retrieve_calibrations(lines)
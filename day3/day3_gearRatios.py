from re import finditer
from typing import List

def read_input(file_name) -> List[str]:
    with open(file_name, 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    return lines


def part1_find_valid_numbers(lines: List[str]) -> int:
    m, n = len(lines), len(lines[0])
    valid_sum = 0
    for r, row in enumerate(lines):
        for num in finditer(r'\d+', row): # find each number in row
            edge = {(edge_r, edge_c) for edge_r in (r - 1, r, r + 1)
                           for edge_c in range(num.start() - 1, num.end() + 1)}

            for edge_r, edge_c in edge:
                if 0 <= edge_r < m and 0 <= edge_c < n and lines[edge_r][edge_c] not in '0123456789.':
                    valid_sum += int(num.group())

    print(valid_sum)
    return valid_sum


if __name__ == '__main__':
    lines = read_input('day3/input.txt')
    part1_find_valid_numbers(lines)

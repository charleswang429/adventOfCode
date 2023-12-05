from collections import defaultdict
from math import prod
from re import finditer
from typing import List, Mapping, Tuple

def read_input(file_name) -> List[str]:
    with open(file_name, 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    return lines


def generate_gear(lines) -> Mapping[Tuple[int, int], List[int]]:
    m, n = len(lines), len(lines[0])
    gears = defaultdict(list)

    for r, row in enumerate(lines):
        for num in finditer(r'\d+', row): # find each number in row
            edge = {(edge_r, edge_c) for edge_r in (r - 1, r, r + 1)
                        for edge_c in range(num.start() - 1, num.end() + 1)}

            for edge_r, edge_c in edge:
                if 0 <= edge_r < m and 0 <= edge_c < n and lines[edge_r][edge_c] not in '0123456789.':
                    gears[(edge_r, edge_c)].append(int(num.group()))
    return gears


def part1_find_valid_numbers(lines: List[str]) -> int:
    gears = generate_gear(lines)
    return sum(sum(gear) for gear in gears.values())


def part2_gear_product(lines: List[str]) -> int:
    gears = generate_gear(lines)
    return sum(prod(gear) for gear in gears.values() if len(gear) == 2)


if __name__ == '__main__':
    lines = read_input('day3/input.txt')
    part1_find_valid_numbers(lines)
    part2_gear_product(lines)

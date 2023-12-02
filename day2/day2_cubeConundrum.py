from collections import defaultdict
from functools import reduce
from re import findall
from typing import List

max_map = {'red': 12, 'green': 13, 'blue': 14}

def read_input() -> List[str]:
    with open('day2/input.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    return lines


def valid_cube_count(game: str) -> bool:
    draws = findall(r"\d+ \w*", game)
    for draw in draws:
        count, color = draw.split()
        if int(count) > max_map[color]:
            return False
    return True


def part1_valid_game(lines: List[str]):
    valid_game = 0
    for line in lines:
        gid, game = line[5:].rstrip('\n').split(': ')
        if valid_cube_count(game):
            valid_game += int(gid)
    return valid_game


def find_power_of_set(game: str) -> int:
    min_map = defaultdict(int)
    draws = findall(r"\d+ \w*", game)
    for draw in draws:
        count, color = draw.split()
        min_map[color] = max(min_map[color], int(count))

    return reduce(lambda a, b: a * b, min_map.values(), 1)

def part2_fewest_cubes(lines: List[str]):
    power_sum = 0
    for line in lines:
        gid, game = line[5:].rstrip('\n').split(': ')
        power_sum += find_power_of_set(game)
    return power_sum


if __name__ == '__main__':
    lines = read_input()
    part1_valid_game(lines)
    part2_fewest_cubes(lines)

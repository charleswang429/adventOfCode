import re
from typing import List

max_map = {'red': 12, 'green': 13, 'blue': 14}

def read_input() -> List[str]:
    with open('day2/input.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    return lines

def valid_cube_count(game: str) -> bool:
    draws = re.findall(r"\d\d? \w*", game)
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
    print(valid_game)
    return valid_game

if __name__ == '__main__':
    lines = read_input()
    part1_valid_game(lines)

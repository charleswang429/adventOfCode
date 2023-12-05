from typing import List


def read_input(file_name) -> List[str]:
    with open(file_name, 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    return lines


def part1_find_points(score_card: List[str]) -> int:
    total_points = 0
    for card in score_card:
        first, nums_str = card.split(' | ')
        _, winning_nums_str = first.split(': ')
        nums, winning_nums = [int(num) for num in nums_str.split()], [int(num) for num in winning_nums_str.split()]
        matches = len(set(nums).intersection(winning_nums))
        total_points += 2 ** (matches - 1) if matches != 0 else 0

    return total_points


if __name__ == '__main__':
    score_card = read_input('day4/input.txt')
    part1_find_points(score_card)

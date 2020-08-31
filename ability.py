import random

ENTROPY = 1000
TOTAL = 72
MIN_SCORE = 6
MAX_SCORE = 17
NUM_ABILITIES = 6

random.seed()


def randomize_abilities(total, min_score, max_score, num_abilities, entropy):
    if max_score * num_abilities < total or min_score * num_abilities > total:
        raise ValueError

    if min_score * num_abilities == total:
        return [min_score] * num_abilities
    if max_score * num_abilities == total:
        return [max_score] * num_abilities

    abilities = [total // num_abilities] * num_abilities
    for _ in range(total % num_abilities):
        abilities[random.randrange(num_abilities)] += 1

    def find_non_matching(val):
        for i in range(num_abilities):
            if abilities[i] != val:
                return i

    for _ in range(entropy):
        num_min = sum(ability == min_score for ability in abilities)
        num_max = sum(ability == max_score for ability in abilities)

        if num_min == num_abilities - 1:
            down = find_non_matching(min_score)
            up = random.randrange(num_abilities - 1)
            if up >= down:
                up += 1
        elif num_max == num_abilities - 1:
            up = find_non_matching(max_score)
            down = random.randrange(num_abilities - 1)
            if down >= up:
                down += 1
        else:
            while True:
                up = random.randrange(num_abilities)
                if abilities[up] < max_score:
                    break
            while True:
                down = random.randrange(num_abilities - 1)
                if down >= up:
                    down += 1
                if abilities[down] > min_score:
                    break

        abilities[up] += 1
        abilities[down] -= 1

    return abilities


print(randomize_abilities(TOTAL, MIN_SCORE, MAX_SCORE, NUM_ABILITIES, ENTROPY))

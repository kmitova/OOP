from itertools import permutations


def possible_permutations(nums):
    result = permutations(nums)
    for perm in result:
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]

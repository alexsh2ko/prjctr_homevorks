'''1. Write a Python program to compute the difference between two lists.

    Sample data: ['a', 'b', 'c', 'd'], ['c', 'd', 'e']

    Expected Output:

    first-second: ['a', 'b']

    second-first: ['e']
'''
first = []
second = []
def compute_difference(first: list, second: list) -> tuple:
    first_second = []
    second_first = [] 
    for val in first:
        if val not in second:
            first_second.append(val)
    for val in second:
        if val not in first:
            second_first.append(val)
    print(f'first-second: {first_second}')
    print(f'second_first: {second_first}')
    return first_second, second_first


def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b', 'c'], ['e'])

    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])

    result3 = compute_difference([1, 2, 3], [4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 5, 6])

    result3 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result3 == ([1], [4])
test_compute_difference()
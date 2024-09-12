# https://www.spoj.com/problems/YODANESS/
from sys import stdin


def merge_sort_c_i(numbers: list):
    if len(numbers) == 1:
        return numbers, 0
    middle = len(numbers) // 2
    half1, counter1 = merge_sort_c_i(numbers[:middle])
    half2, counter2 = merge_sort_c_i(numbers[middle:])
    result, counter3 = merge(half1, half2)
    return result, counter1 + counter2 + counter3


def merge(list1: list, list2: list):
    result = []
    inversion_counter = 0
    n = len(list1)
    m = len(list2)
    i = 0
    j = 0
    while i < n and j < m:
        while i < n and j < m and list1[i] > list2[j]:
            result.append(list2[j])
            inversion_counter += n - i
            j += 1
        while i < n and j < m and list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
    while i < n:
        result.append(list1[i])
        i += 1
    while j < m:
        result.append(list2[j])
        j += 1
    return result, inversion_counter


t_c = int(stdin.readline())
for i in range(t_c):
    n = int(stdin.readline())
    unordered_list = stdin.readline().split()
    sorted_list = stdin.readline().split()
    sorted_dict = {word: index for index, word in enumerate(sorted_list)}
    unordered_indexes = [sorted_dict[word] for word in unordered_list]
    sorted_list2, count = merge_sort_c_i(unordered_indexes)
    print(count)

# 3
# from datetime import date  # Python code for task 3

# s = date(2010, 8, 9)  # CP1 launch date
# t = date.today()
# print(s.strftime("%A"))  # 'Mon', %A for 'Monday'
# print("{} day(s) ago".format((t - s).days))

# 5
# dates = [(29, 2, 1976), (29, 2, 1974), (3, 4, 1997), (26, 8, 1995)]
# dates.sort(key=lambda item: (item[1], item[0], -item[2]))
# print(dates)

# 7
from itertools import permutations

array = "ABC"
print(*permutations(array), sep="\n")


# 8
# array = ["a", "b", "c"]
# n = len(array)
# for i in range(1 << n):
#     current_subset = ""
#     for j in range(n):
#         if 1 << j & i:
#             current_subset += array[j]
#     print(current_subset)


# 9
# number_input = "FF"
# base_from = 16
# base_to = 2
# remainders = [chr(i) for i in range(ord("0"), ord("9") + 1)] + [
#     chr(i) for i in range(ord("A"), ord("Z") + 1)
# ]
# rem_dict = {char: index for index, char in enumerate(remainders)}
# number_base10 = 0
# for i in range(len(number_input)):
#     number_base10 += pow(base_from, i) * rem_dict[number_input[-i - 1]]
# number_output = ""
# while number_base10 > 0:
#     number_output = remainders[number_base10 % base_to] + number_output
#     number_base10 //= base_to
# print(number_output)

# 12
# expression = "3 + (8 - 7.5) * 10 / 5 - (2 + 5 * 7)"
# print(eval(expression))

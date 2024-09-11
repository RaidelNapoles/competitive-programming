# https://www.spoj.com/problems/MIB/
from math import factorial
from sys import stdin


t_c = int(stdin.readline())
for i in range(t_c):
    n = int(stdin.readline())
    word_list = stdin.readline().split()
    sorted_list = sorted(word_list)
    fact = factorial(n)
    order = 1
    for i in range(len(word_list)):
        rest = n - i
        divisor = rest if rest >= 1 else 1
        fact //= divisor

        index = sorted_list.index(word_list[i])
        order += fact * index

        sorted_list.remove(word_list[i])
    print(order)

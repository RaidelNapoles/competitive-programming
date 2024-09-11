# https://www.spoj.com/problems/INTEST/
import os


instance = list(map(int, os.read(0, 2 + 12 * int(1e7)).split()))
n, k = instance[:2]
print(len(list(filter(lambda x: x % k == 0, instance[2:]))))

# https://prologin.org/train/2012/semifinal/retour_vers_le_futur
import os


instance = list(map(int, os.read(0, 1 + 10 * int(1e7)).split()))
n = instance[0]
s = [(instance[i], instance[i + 1]) for i in range(1, 2 * n, 2)]
b = [(start, -1) for start, end in s] + [(end, 1) for start, end in s]
b.sort()
count = 0
best = 0
for i, j in b:
    count += j
    best = min(best, count)
print(-best)

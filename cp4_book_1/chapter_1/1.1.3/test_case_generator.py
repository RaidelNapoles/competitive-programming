import random


# 1 ≤ 𝑁 ≤ 8
# 0 ≤ 𝑥, 𝑦 ≤ 1000
def generate_test_case(n=None):
    if not n:
        n = random.randint(1, 8)
    locations = [
        (random.randint(0, 1000), random.randint(0, 1000)) for _ in range(2 * n)
    ]
    return locations


if __name__ == "__main__":
    locations = generate_test_case()
    print(len(locations))
    for loc in locations:
        print(loc)

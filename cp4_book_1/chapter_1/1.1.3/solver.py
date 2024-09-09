import math
from utils import measure_time

max_sum = 1e9


def naive_solver_bt(locations: list, mask: list, pos: int, current_sum: float):
    global max_sum
    if pos >= len(locations) or all(mask):
        max_sum = min(max_sum, current_sum)
        return

    leader_pos = pos
    for i in range(leader_pos, len(locations)):
        if not mask[i]:
            leader_pos = i
            mask[i] = True
            break

    partner_pos = leader_pos + 1
    for i in range(partner_pos, len(locations)):
        if not mask[i]:
            partner_pos = i
            mask[i] = True

            leader = locations[leader_pos]
            partner = locations[partner_pos]
            group_distance = math.dist(leader, partner)
            naive_solver_bt(
                locations, mask, leader_pos + 1, current_sum + group_distance
            )

            mask[i] = False

    mask[leader_pos] = False


max_sum_pruned = 1e9


def naive_pruned_solver_bt(locations: list, mask: list, pos: int, current_sum: float):
    global max_sum_pruned
    if current_sum > max_sum_pruned:
        return
    if pos >= len(locations) or all(mask):
        max_sum_pruned = min(max_sum_pruned, current_sum)
        return

    leader_pos = pos
    for i in range(leader_pos, len(locations)):
        if not mask[i]:
            leader_pos = i
            mask[i] = True
            break

    partner_pos = leader_pos + 1
    for i in range(partner_pos, len(locations)):
        if not mask[i]:
            partner_pos = i
            mask[i] = True

            leader = locations[leader_pos]
            partner = locations[partner_pos]
            group_distance = math.dist(leader, partner)
            naive_pruned_solver_bt(
                locations, mask, leader_pos + 1, current_sum + group_distance
            )

            mask[i] = False

    mask[leader_pos] = False


@measure_time
def naive_solver(locations: list):
    mask = [False for _ in range(len(locations))]
    naive_solver_bt(locations, mask, 0, 0)
    return max_sum


@measure_time
def naive_solver_pruned(locations: list):
    mask = [False for _ in range(len(locations))]
    naive_pruned_solver_bt(locations, mask, 0, 0)
    return max_sum_pruned


# # first test case
# locations = [(1, 1), (8, 6), (6, 8), (1, 3)]
# print(naive_solver(locations))
# print(naive_solver_pruned(locations))

def can_feed_hamsters(s, c, hamsters, mid):
    hamsters.sort(key=lambda x: (x[1]))
    total_food = 0

    for i in range(mid):
        food_needed = hamsters[i][0] + i * hamsters[i][1]
        total_food += food_needed

    return total_food


def max_hamsters(s, c, hamsters):
    left, right = 0, c
    result = 0

    while left <= right:
        mid = left + (right - left)
        if can_feed_hamsters(s, c, hamsters, mid) < s:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


def total_food_needed(hamsters):
    total_food = 0

    for i in range(len(hamsters)):
        food_needed = hamsters[i][0] + hamsters[i][1] * (len(hamsters)-1)
        total_food += food_needed

    return total_food


s = 35
c = 4
hamsters = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(max_hamsters(s, c, hamsters))
print(total_food_needed(hamsters))

s = 19
c = 4
hamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]
print(max_hamsters(s, c, hamsters))

s = 2
c = 2
hamsters = [[1, 50000], [1, 60000]]
print(max_hamsters(s, c, hamsters))

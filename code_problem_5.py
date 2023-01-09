def max_height(bricks, step_num):
    # Using formula for sum of arithmetical progression to find max height for smallest step
    # 1 Equalizing the steps with the far right one
    equalized_bricks = bricks - (step_num - 1) * step_num / 2
    # 2 Cutting of left bricks and getting max height
    return int((equalized_bricks - (equalized_bricks % step_num)) / step_num)


def create_staircases_counter():
    cache = {}

    def counter(bricks, step):
        key = str(bricks) + '_' + str(step)

        if key in cache:
            return cache.get(key)

        if step == 2:
            return max_height(bricks, step)

        result = 0

        for x in range(1, max_height(bricks, step) + 1):
            result += counter(bricks - x * step, step - 1)

        cache[key] = result

        return result

    return counter


def solution(n):
    staircases_counter = create_staircases_counter()
    combinations = 0
    minimal_step_number = 2

    # Using formula for sum of arithmetical progression to find max length
    max_length = int((-1 + (1 + 8 * n) ** 0.5) / 2)

    for step in range(minimal_step_number, max_length + 1):
        combinations += staircases_counter(n, step)

    return combinations


# r = solution(200)

# print(r)
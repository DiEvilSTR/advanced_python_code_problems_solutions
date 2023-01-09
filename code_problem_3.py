def solution(x, y):
    # Putting bunnies in order
    max_len = x + y - 1
    max_number_x = max_len * (max_len + 1) / 2
    result = max_number_x - (max_len - x)
    
    return str(int(result))


# print(solution(3, 2))
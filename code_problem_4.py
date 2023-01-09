def solution(n):
    m = int(n)
    turns = 0
    while m != 1:
        if m % 2 == 0:
            m //= 2
        elif m == 3 or m % 4 == 1:
            m -= 1
        else:
            m += 1
        turns += 1
    
    return int(turns)

# print(solution(15))
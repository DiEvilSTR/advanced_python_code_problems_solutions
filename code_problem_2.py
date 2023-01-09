def sorting_alg(x):
    splitted_ver = list(x.split("."))
    return [int(i) for i in splitted_ver]


def solution(l):
    return sorted(l, key=sorting_alg)

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))